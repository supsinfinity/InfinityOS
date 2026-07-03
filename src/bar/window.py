import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class InfinityWindow(Gtk.ApplicationWindow):
    def __init__(self, application):
        super().__init__(application=application)

        self.set_title("∞ InfinityOS")
        self.set_default_size(1000, 60)
        self.set_resizable(False)

        # Create the main layout
        center_box = Gtk.CenterBox()
        center_box.set_margin_start(20)
        center_box.set_margin_end(20)
        center_box.set_margin_top(10)
        center_box.set_margin_bottom(10)

        # Left section
        infinity = Gtk.Label(label="∞")

        # Center section
        music = Gtk.Label(label="🎵 No music playing")

        # Right section
        clock = Gtk.Label(label="🕒 00:00")

        # Add widgets to the CenterBox
        center_box.set_start_widget(infinity)
        center_box.set_center_widget(music)
        center_box.set_end_widget(clock)

        # Make the CenterBox the window contents
        self.set_child(center_box)