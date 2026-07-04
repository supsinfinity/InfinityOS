import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class ContextComponent:
    def __init__(self):
        self.widget = Gtk.Label(
            label="🎵 No music playing"
        )
        self.widget.set_name("context")

    def set_text(self, text):
        self.widget.set_label(text)