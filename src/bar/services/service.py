class Service:
    """
    Base class for all InfinityOS services.

    Services own application state and business logic.

    Every service provides a consistent lifecycle through
    the start() and stop() methods.
    """

    def __init__(self):
        self.running = False

    def start(self):
        """Start the service."""
        self.running = True

    def stop(self):
        """Stop the service."""
        self.running = False

    @property
    def is_running(self):
        return self.running
    
    def get_services(self):
        """
        Return every registered service.
        """
        return list(self.services)