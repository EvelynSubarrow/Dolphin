class EventTree:
    def __init__(self, name, root=None):
        self._root = root
        self._trees = {}
        self._hooks = set()

    def _guarantee_tree(self, tree_name):
        if tree_name not in self._trees:
            self._trees[tree_name] = EventTree(tree_name, self)
        return self._trees[tree_name]

    def single(self, event_name):
        current_tree = self
        for part in event_name.split("/"):
            current_tree = current_tree._guarantee_tree(part)
        return current_tree

    def __getitem__(self, event_name):
        return self.single(event_name)

    def hook(self, module_instance, function_reference, priority=1000):
        self._hooks.add((module_instance, function_reference, priority))

    def __call__(self, *args, **kwargs):
        for module_instance, function_reference, priority in sorted(self._hooks, key=lambda m,f,p: p):
            function_reference(module_instance, *args, **kwargs)
        if self._root:
            self._root(*args,**kwargs)
