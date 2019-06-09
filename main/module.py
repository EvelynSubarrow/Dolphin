class Module:
    # This is called when a module is enabled after loading
    def on_enable(self, main):
        pass

    # This is called when a module is disabled
    def on_disable(self, main):
        pass

    # This is called when a module is loaded, before enabling
    def on_load(self, main):
        pass

    # This is called when a module is unloaded
    def on_unload(self, main):
        pass

    # This is called when a module is reloaded (in addition to on_load and on_unload)
    def on_reload(self, main):
        pass

    # This is used to transfer a module's state when reloading
    def deconstitute(self):
        return None

    # This is used to restore a module's state. Returns bool reflection of success
    def reconstitute(self, state):
        return True
