import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from .launcher_menu import LauncherMenu

class InfinityComponent:
    """
    Displays the Infinity launcher button.
    Acts as the primary entry point for InfinityOS features
    and provides access to the LauncherMenu.
    """
    def __init__(self):
        self.widget = Gtk.MenuButton()
        self.widget.set_label("∞")
        self.widget.set_name("infinity")

        self.launcher = LauncherMenu()
        self.widget.set_popover(self.launcher.popover)