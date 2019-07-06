from main.module import Module

class Module(Module):
    def __init__(self, main):
        self.main = main

    def on_enable(self, main):
        main.config = self

    # Individual items, default response hooks should be registered north of 0
    def __getitem__(self, key):
        responses = self.main.events["config/collect/{}".format(key)](key)
        if len(responses):
            return responses[0]
        else:
            return None

    # This is for the likes of irc/server/*, defaults shouldn't be provided or
    # requested
    # TODO: condense all keys across all responses
    def get_keys(self, key):
        return self.main.events["config/keys/{}".format(key)](key)[0]
