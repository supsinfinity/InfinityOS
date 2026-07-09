from datetime import datetime

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib


class ClockComponent:
    def __init__(self):
        self.widget = Gtk.Label()
        self.widget.set_name("clock")

        self.update()
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        self.widget.set_label(
            datetime.now().strftime("🕒 %I:%M:%S %p")
        )
        return True