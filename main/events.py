class EventTree:
    def __init__(self, name):
        self._trees = {}
        self._hooks = set()

    def _guarantee_tree(self, tree_name):
        if tree_name not in self._trees:
            self._trees[tree_name] = EventTree(tree_name)
        return self._trees[tree_name]

    def single(self, event_name):
        current_tree = self
        for part in event_name.split("/"):
            current_tree = current_tree._guarantee_tree(part)
        return current_tree

    def __getitem__(self, event_name):
        return self.single(event_name)

    def hook(self, module_instance, function_reference):
        self._hooks.add((module_instance, function_reference))

    def invoke(self, event_name, event):
        current_tree = self
        for part in event_name.split("/"):
            current_tree = current_tree._guarantee_tree(part)
            current_tree._invoke(event)

    def _invoke(self, event):
        for module_instance, function_reference in self._hooks:
            function_reference(module_instance, event)

class Event:
    pass
