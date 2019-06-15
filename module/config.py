import os
from collections import OrderedDict

from main.module import Module

class Module(Module):
    def __init__(self, main):
        self._main = main

    def on_enable(self, main):
        main.config = self

    # Individual items, default response hooks should be registered north of 0
    def __getitem__(self, key):
        main.events["config/collect/{}".format(key)](key)

    # This is for the likes of irc/server/*, defaults shouldn't be provided or
    # requested
    def get_keys(self, key):
        main.events["config/keys/{}".format(key)](key)
