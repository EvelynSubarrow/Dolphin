import importlib.util, importlib.abc, typing, sys

from main.module import Module

class Module(Module):
    def __init__(self, main):
        self.modules = {}
        self.current_index = 0

    def load_module(self, name):
        self.current_index += 1
        self._load_module(name, "module/{}:{:04X}".format(name, self.current_index), "module/{}.py".format(name))

    def _load_module(self, short_name, name, path):
        module_spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(module_spec)

        loader = typing.cast(importlib.abc.Loader, module_spec.loader)
        loader.exec_module(module)

        module.instance = module.Module(self)
        module.id = self.current_index
        module.enabled = True

        self.modules[short_name] = module
