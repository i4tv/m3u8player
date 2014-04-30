# -*- coding: UTF-8 -*-

from m3u8player.controller import M3U8Controller
__controller__ = M3U8Controller

# Registering a new player
from mediacore.lib.players import AbstractFlashPlayer
from m3u8player.player import M3U8Player
AbstractFlashPlayer.register(M3U8Player)

# import will trigger execution of observers.py so observers declared there are
# known to MediaCore
import m3u8player.observers

