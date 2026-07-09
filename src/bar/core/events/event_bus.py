class EventBus:
    """
    Provides publish-subscribe communication throughout InfinityOS.

    The EventBus allows services to notify interested components
    when application state changes while keeping modules loosely
    coupled.

    Events act as notifications rather than data containers.
    """

    def __init__(self):
        self._listeners = {}
        
    def subscribe(self, event_name, callback):
        """
        Register a callback for an event.
        """

        if event_name not in self._listeners:
            self._listeners[event_name] = []

        self._listeners[event_name].append(callback)

    def emit(self, event_name, *args, **kwargs):
        """
        Notify every listener that an event occurred.
        """

        listeners = list(self._listeners.get(event_name, []))

        for callback in listeners:
            callback(*args, **kwargs)
    
    def unsubscribe(self, event_name, callback):
        """
        Remove a callback from an event.
        """

        listeners = self._listeners.get(event_name)

        if not listeners:
            return

        if callback in listeners:
            listeners.remove(callback)

        if not listeners:
            del self._listeners[event_name]

    def has_listeners(self, event_name):
        """
        Return True if the event has listeners.
        """
        return event_name in self._listeners