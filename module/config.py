from main.module import Module

class Module(Module):
    def on_enable(self, main):
        main.config = self
