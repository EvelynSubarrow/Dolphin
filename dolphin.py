#!/usr/bin/env python3

import importlib.util, importlib.abc, typing, sys

from main import events

class Main:
    def __init__(self):
        self.events = events.EventTree("/")
        self.modules = None

    def main(self):
        self.load_module_loader()
        self.events["start"]()

    def load_module_loader(self):
        module_spec = importlib.util.spec_from_file_location("module/module_loader", "module/ModuleLoader.py")
        module = importlib.util.module_from_spec(module_spec)

        loader = typing.cast(importlib.abc.Loader, module_spec.loader)
        loader.exec_module(module)

        module.instance = module.ModuleLoader(self)

        self.modules = module.instance

if __name__=="__main__":
    main = Main().main()
