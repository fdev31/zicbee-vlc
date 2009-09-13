import os
import sys
from time import sleep

SONGNAME = 'cocos2d_oh_yeah.mp3'

class TestPlayer(object):
    def setUp(self):
        from zicbee_vlc import Player
        self.player = Player()
        self.player.load(SONGNAME)
        sleep(0.5)

    def tearDown(self):
        sleep(0.2)
        self.player.quit()

    def test_position(self):
        assert isinstance(self.player.position, int)

    def test_seek(self):
        self.player.seek(-1)

    def test_reload(self):
        self.player.load(SONGNAME)

    def test_cache(self):
        self.player.set_cache(128)
        self.player.set_cache(4096)

    def test_pause(self):
        self.player.pause()
        self.player.pause()

    def test_volume(self):
        for n in xrange(10):
            sleep(0.1)
            self.player.volume(n*10)

