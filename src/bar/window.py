import gi
from datetime import datetime
from pathlib import Path

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib, Gdk

from core.logger import logger
from components.context import ContextComponent
from components.launcher import InfinityComponent
from components.layout import StatusAreaComponent
from core.constants import BAR_HEIGHT

from services.weather_service import WeatherService

class InfinityWindow(Gtk.ApplicationWindow):
    """
    Main application window for the Infinity Bar.
    Constructs the visual layout by arranging UI
    components while delegating application logic
    to InfinityCore and registered services.
    The window is responsible only for presentation
    and layout.
    """
    def __init__(self, application, core):
        super().__init__(application=application)

        self.application = application
        self.core = core

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
        infinity = InfinityComponent()
        center_box.set_start_widget(infinity.widget)

        # Center
        context = ContextComponent()
        center_box.set_center_widget(context.widget)

        # Right
        self.status_area = StatusAreaComponent(core)

        right_box = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=12,
        )

        right_box.append(self.status_area.widget)

        center_box.set_end_widget(right_box)
        self.set_child(center_box)

    def on_realize(self, *args):
        logger.info("Infinity Bar initialized")