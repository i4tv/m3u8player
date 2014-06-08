# -*- coding: UTF-8 -*-

from mediacore.lib.players import AbstractFlashPlayer
from mediacore.lib.util import url_for

class M3U8Player(AbstractFlashPlayer):
    name = u'm3u8player'
    display_name = u'M3U8 Player'

    supported_containers = set(['m3u8'])
    supported_schemes = set(['http'])

    def swf_url(self):
        """Return the flash player URL."""
        return url_for('/m3u8player/public/scripts/third-party/HLSProviderChromeless.swf', qualified=self.qualified)

    # you could override flashvars() for example to add player some options
    def flashvars(self):
        """Return a python dict of flashvars for this player."""
        return {}
