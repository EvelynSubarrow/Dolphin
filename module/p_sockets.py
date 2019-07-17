import socket

from multiprocessing.pool import ThreadPool

from main.module import Module

class Module(Module):
    def __init__(self, main):
        self.main = main

    def on_enable(self, main):
        self._pool = ThreadPool(2)

    def on_disable(self, main):
        self._pool.close()
        self._pool.join()

    def _form_socket(self, family, address, port, identifier, event_path, event_queue):
        s = socket.socket(family)
        s.settimeout(5)
        s.connect((address, port))
        event_queue.put({"path": event_path, "args": {"socket": s, "id": identifier}})

    def queue(self, family, address, port, identifier, event_path):
        self._pool.apply_async(self._form_socket, [family, address, port, identifier, event_path, self.main.events.internal_queue])
