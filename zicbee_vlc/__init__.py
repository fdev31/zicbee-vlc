# TODO: export fetch_playlist & playlist handling out of player class
__all__ = ['Player']

from .vlc import Instance

class Player(object):
    def __init__(self):
        self.vlc = Instance()
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
        self.p.play()

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
            return self.p.get_position()*100


