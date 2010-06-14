__all__ = ['Player']

from . import vlc

class Player(object):
    _finished = False
    def __init__(self):
        self.vlc = vlc.Instance()
        self.p = None

    def set_cache(self, val):
        """ Sets the cache value in kilobytes """
        pass

    def volume(self, val):
        """ Sets volume [0-100] """
        self.vlc.audio_set_volume(val)

    def seek(self, val):
        """ Seeks specified number of seconds (positive or negative) """
        if self.p:
            self.p.set_position(val/100.0 + self.p.get_position())

    def pause(self):
        """ Toggles pause mode """
        if self.p:
            self.p.pause()

    def respawn(self):
        """ Restarts the player """
        if self.p:
            self.p.stop()

    def load(self, uri):
        """ Loads the specified URI """
        if self.p:
            self.p.stop()
        self.p = self.vlc.media_player_new(uri)
        Player._finished = False
        e = self.p.event_manager()
        e.event_attach(vlc.EventType.MediaPlayerEndReached, self.__end_reached, None)
        try:
            if not ('://' in uri and not uri.startswith('file')) and self.p.will_play() != 1:
                raise ValueError("Won't play")
        except: # ValueError or any VLC Error
            self._finished = True
        else:
            self.p.play()

    @vlc.callbackmethod
    def __end_reached(event, plr):
        Player._finished = True

    def quit(self):
        """ De-initialize player and wait for it to shut down """
        try:
            if self.p:
                self.p.stop()
        except Exception, e:
            print "E: %s"%e

    @property
    def position(self):
        """ returns the stream position, in seconds """
        if self.p:
            if self._finished:
                return None
            return self.p.get_position()*10


