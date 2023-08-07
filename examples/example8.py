import time


class EventManager:
    def __init__(self):
        self.events = {}

    def on(self, event_name, handler):
        if event_name not in self.events:
            self.events[event_name] = []
        self.events[event_name].append(handler)

    def emit(self, event_name, data=None):
        if event_name in self.events:
            for handler in self.events[event_name]:
                handler(data)

    def off(self, event_name, handler):
        if event_name in self.events:
            if handler in self.events[event_name]:
                self.events[event_name].remove(handler)


# We create a class that will emit the events
class EmitterEvents:
    def __init__(self, manager_event):
        self.event_manager = manager_event

    def emit_event(self, event_name, data=None):
        self.event_manager.emit(event_name, data)


# Class that will handle the events
class HandlerEvents:
    def __init__(self, manager_event):
        self.event_manager = manager_event
        self.event_manager.on('custom_event', self.manager)

    def manager(self, data):
        print(f"Customized handler executed with the following data: {data}")


def start_handler():
    # We create an instance of the EventManager
    event_manager = EventManager()

    # Create instances of the sender and the handler
    emitter = EmitterEvents(event_manager)
    handler = HandlerEvents(event_manager)

    # We issue the custom event 'my_event' with some data
    emitter.emit_event('custom_event', {"message": "Personalized event!"})

    # We can remove the custom handler after some time if desired

    def remove_manager():
        event_manager.off('custom_event', handler.manager)

    # We remove the handler after 5 seconds
    time.sleep(5)
    remove_manager()

    # We emit the event again to see that the handler is no longer executed.
    emitter.emit_event('custom_event', {"message": "This message will not be displayed"})
