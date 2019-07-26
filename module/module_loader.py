import importlib.util, importlib.abc, typing, sys

from main.module import Module

class Module(Module):
    def __init__(self, main):
        self.modules = {}
        self.current_index = 0
        self.main = main

    def __getitem__(self, name):
        return self.modules[name].instance

    def on_enable(self, main):
        main.modules = self
        main.events["start"].hook(self.initial_load)

    def enable_module(self, name):
        self.modules[name].enabled = True
        self.modules[name].instance.on_enable(self.main)
        self.main.events["module_loader/module/enable/{}".format(name)](name=name)

    def disable_module(self, name):
        self.modules[name].enabled = False
        self.modules[name].instance.on_disable(self.main)
        self.main.events["module_loader/module/disable/{}".format(name)](name=name)

    def initial_load(self, event):
        for module_name in self.main.config.get_keys("module/module_loader/modules"):
            self.load_module(module_name)

    def load_module(self, name):
        self.current_index += 1
        self._load_module(name, "{}__{}".format(name, self.current_index), "module/{}.py".format(name))

    def _load_module(self, short_name, name, path):
        if any(self.main.events["module_loader/module/preload/{}".format(short_name)](name=name, id=self.current_index)):
            return

        module_spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(module_spec)

        loader = typing.cast(importlib.abc.Loader, module_spec.loader)
        loader.exec_module(module)

        module.instance = module.Module(self.main)
        module.id = self.current_index
        module.enabled = False

        self.modules[short_name] = module

        module.instance.on_load(self.main)
        self.enable_module(short_name)
        self.main.events["module_loader/module/load/{}".format(short_name)](name=name)


    def unload_module(self, name):
        self.disable_module(name)
        self.modules[name].instance.on_unload(self.main)
        del self.modules[name]
        self.main.events["module_loader/module/unload/{}".format(name)](name=name)
