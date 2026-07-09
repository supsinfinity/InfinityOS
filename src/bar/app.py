import gi
from core.core import InfinityCore

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from window import InfinityWindow


class InfinityBarApplication(Gtk.Application):
    """
    Main GTK application for InfinityOS.
    Initializes the application's infrastructure,
    creates the main window, and starts all
    registered services during application startup.
    """
    def __init__(self):
        super().__init__(application_id="com.infinityos.bar")

    def do_activate(self):
        core = InfinityCore()
        core.start()

        window = InfinityWindow(
        application=self,
        core=core,
        )

        window.present()