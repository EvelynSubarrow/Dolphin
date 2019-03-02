#!/usr/bin/env python3

from main import events

class Main:
    def __init__(self):
        self.events = events.EventTree("/")
        self.modules = None

if __name__=="__main__":
    main = Main()
