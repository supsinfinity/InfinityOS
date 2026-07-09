class Backend:
    """
    Base class for all InfinityOS backends.
    """

    def initialize(self):
        """
        Prepare backend resources.
        """
        pass

    def shutdown(self):
        """
        Clean up backend resources.
        """
        pass