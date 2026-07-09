from gi.repository import Gtk


class Component:
    """
    Base class for all InfinityOS UI components.

    Provides a common GTK widget, automatic event subscription,
    and convenient access to registered services.

    Components are responsible only for presenting information
    to the user.
    """

    EVENT = None

    def __init__(self, core):
        self.core = core
        self.widget = Gtk.Label()

        if self.EVENT:
            self.core.get_event_bus().subscribe(
                self.EVENT,
                self.refresh,
            )

    def get_service(self, service_type):
        return (
            self.core
            .get_service_manager()
            .get_service(service_type)
        )

    def refresh(self) -> None:
        """
        Override in subclasses.
        """
        pass