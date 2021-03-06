from collections import OrderedDict

from main.module import Module

class Module(Module):
    def __init__(self, main):
        self.main = main

    def on_enable(self, main):
        main.config = self

    # Individual items, default response hooks should be registered north of 0
    def __getitem__(self, key):
        responses = self.main.events["config/collect/{}".format(key)](key=key)
        # TODO: more helpful (and specific) error
        return responses[0]

    def get(self, key, default=None):
        responses = self.main.events["config/collect/{}".format(key)](key=key)
        if len(responses):
            return responses[0]
        else:
            return default

    # This is for the likes of irc/server/*, defaults shouldn't be provided or
    # requested
    def get_keys(self, key):
        return OrderedDict.fromkeys(sum(self.main.events["config/keys/{}".format(key)](key=key),[])).keys()
