import gi
from datetime import datetime
from pathlib import Path

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib, Gdk

from components.clock import ClockComponent
from components.context import ContextComponent
from components.infinity import InfinityComponent
class InfinityWindow(Gtk.ApplicationWindow):
    def __init__(self, application):
        super().__init__(application=application)

        BAR_HEIGHT = 30
        TOP_MARGIN = 8
        SIDE_MARGIN = 24
        # Load CSS
        provider = Gtk.CssProvider()
        css_path = Path(__file__).parent / "style.css"
        provider.load_from_path(str(css_path))

        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )

        self.set_title("∞ InfinityOS")
        self.set_decorated(False)
        self.set_default_size(1200, 30)
        self.set_resizable(False)

        # Main layout
        center_box = Gtk.CenterBox()
        center_box.set_margin_start(20)
        center_box.set_margin_end(20)
        center_box.set_margin_top(10)
        center_box.set_margin_bottom(10)

        # Left
        infinity=InfinityComponent()
        center_box.set_start_widget(infinity.widget)

        # Center
        context = ContextComponent()
        center_box.set_center_widget(context.widget)

        # Right
        clock=ClockComponent()
        center_box.set_end_widget(clock.widget)

        # Add widgets
        center_box.set_start_widget(infinity.widget)
        center_box.set_center_widget(context.widget)
        center_box.set_end_widget(clock.widget)

        self.set_child(center_box)

        self.connect("realize", self.on_realize)
       
    def on_realize(self, *args):
        print("Infinity Bar initialized")