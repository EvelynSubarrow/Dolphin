import time

from main.module import Module
from main.events import event_hook

class Module(Module):
    def __init__(self, main):
        self.main = main
        self.last_ut = 0

    @event_hook("tick")
    def tick(self, event):
        ut_now = time.time()

        # The aim is for roughly four ticks per second
        time.sleep(max(0, .25-(ut_now-self.last_ut)))

        self.last_ut = ut_now

        print("tick")
