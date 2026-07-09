class BackendManager:
    """
    Manages the lifecycle of all backend implementations.

    Backends provide access to operating system functionality
    such as CPU information, battery status, networking,
    and desktop APIs.

    The BackendManager centralizes backend registration and lookup.
    """

    def __init__(self):
        self.backends = []

    def register(self, backend):
        self.backends.append(backend)

    def get_backend(self, backend_type):
        for backend in self.backends:
            if isinstance(backend, backend_type):
                return backend

        return None