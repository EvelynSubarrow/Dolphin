import json, collections
from pathlib import Path

from main.module import Module

class Module(Module):
    def __init__(self, main):
        self.main = main
        self._config = collections.OrderedDict()

    def on_enable(self, main):
        main.events["config/collect"].hook(self, self.collect)
        main.events["config/keys"].hook(self, self.keys)

    def on_load(self, main):
        self._config = self.reload()

    def reload(self):
        out = collections.OrderedDict()

        for filename in Path("config").glob("**/*.json"):
            config_root_path = str(filename.relative_to(Path("config"))).replace(".json", "")

            with open(str(filename)) as f:
                self.fold(out, json.load(f), config_root_path.split("/"))

        return out

    def fold(self, target_map, source_map, path):
        for k in path:
            if k not in target_map:
                target_map[k] = collections.OrderedDict()
            target_map = target_map[k]

        for k,v in source_map.items():
            if isinstance(v, collections.Mapping):
                self.fold(target_map, v, k.split("/"))
            else:
                target_map[k] = v

    def collect(self, key):
        return self._config.get(key)

    def keys(self, key):
        return self._config.get(key).keys()

