from main.module import Module

class Module(Module):
    def __init__(self, main):
        pass

    def on_enable(self, main):
        main.config = self
