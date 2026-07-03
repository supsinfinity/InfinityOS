import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from window import InfinityWindow


class InfinityBarApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.infinityos.bar")

    def do_activate(self):
        window = InfinityWindow(application=self)
        window.present()