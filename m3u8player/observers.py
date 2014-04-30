# -*- coding: UTF-8 -*-

from mediacore.plugin.events import observes
from mediacore.plugin import events

@observes(events.Environment.loaded)
def on_environment_load(config):
    print 'loaded config'


