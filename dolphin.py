#!/usr/bin/env python3

from main import events
from modules import ModuleLoader

class Main:
    def __init__(self):
        self.events = events.EventTree("/")
        self.modules = None

    def main(self):
        self.events["dolphin/start"]()

if __name__=="__main__":
    main = Main().main()
