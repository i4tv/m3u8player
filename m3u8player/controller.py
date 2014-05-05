# -*- coding: UTF-8 -*-

from mediacore.lib.base import BaseController
from mediacore.lib.decorators import expose

class M3U8Controller(BaseController):
    @expose('m3u8player/m3u8_page.html')
    def m3u8_page(self, tag_name, **kwargs):
        # do your backend work here
        # …
        return {'tag_name': tag_name}

