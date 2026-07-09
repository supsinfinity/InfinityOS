from gi.repository import Gtk

from core.logger import logger
class LauncherMenu:
    def __init__(self):
        """
    Provides the InfinityOS launcher interface.

    Contains actions such as Focus Mode, Dashboard,
    Settings, and future application commands.

    Displayed through a Gtk.Popover attached to the
    Infinity button.
    """

        self.popover = Gtk.Popover()
        self.popover.add_css_class("infinity-launcher")
        self._build_ui()

    def on_dashboard_clicked(self, button):
        logger.debug("Dashboard clicked")
        self.popover.popdown()

    def on_focus_clicked(self, button):
        logger.debug("Focus Mode clicked")
        self.popover.popdown()

    def on_settings_clicked(self, button):
        logger.debug("Settings clicked")
        self.popover.popdown()

    def on_quit_clicked(self, button):
        window = self.popover.get_root()
        application = window.get_application()
        application.quit()

    def _build_ui(self):
        # Main container
        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
            margin_top=8,
            margin_bottom=8,
            margin_start=8,
            margin_end=8,
        )

        box.add_css_class("launcher-box")

        self.popover.set_child(box)

        dashboard = self._create_button(
            "Dashboard",
            self.on_dashboard_clicked,
)

        focus = self._create_button(
            "Focus Mode",
             self.on_focus_clicked,
)

        settings = self._create_button(
            "Settings",
            self.on_settings_clicked,
)
        quit_button = self._create_button(
            "Quit",
            self.on_quit_clicked,
)

        box.append(dashboard)
        box.append(focus)
        box.append(settings)

        separator = Gtk.Separator(
            orientation=Gtk.Orientation.HORIZONTAL
        )
        box.append(separator)

        box.append(quit_button)
    def _create_button(self, label, callback):
        button = Gtk.Button(label=label)
        button.connect("clicked", callback)
        return button