#!/usr/bin/env python3

import importlib.util, importlib.abc, typing, sys

from main import events
from module import module_loader

class Main:
    def __init__(self):
        self.events = events.EventTree("/")
        self.modules = None
        self.config = None

    def main(self):
        self.load_module_loader()
        self.modules.load_module("config")
        self.events["start"]()

    def load_module_loader(self):
        initial_loader = module_loader.Module(self)
        initial_loader.load_module("module_loader")

if __name__=="__main__":
    main = Main().main()
