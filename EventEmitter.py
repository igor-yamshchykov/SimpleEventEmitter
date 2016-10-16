class EventEmitter:
    """ EventEmitter class """

    def __init__(self):
        self.events = {}

    def on(self, name, listener):
        try:
            self.events[name] = self.events[name]
        except KeyError:
            self.events[name] = []
        self.events[name].append(listener)

    def emit(self, name, *args):
        if name in self.events:
            for listener in self.events[name]:
                try:
                    listener(*args)
                except TypeError:
                    listener()

    def remove_listener(self, name, listener):
        if name in self.events and listener in self.events[name]:
            self.events[name].remove(listener)
