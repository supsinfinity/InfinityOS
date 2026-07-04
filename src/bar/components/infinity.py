import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class InfinityComponent:
    def __init__(self):
        self.widget = Gtk.MenuButton()
        self.widget.set_label("∞")
        self.widget.set_name("infinity")

        popover = Gtk.Popover()

        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
        )
        box.set_margin_top(10)
        box.set_margin_bottom(10)
        box.set_margin_start(10)
        box.set_margin_end(10)

        for text in [
            "Focus Mode",
            "Launcher",
            "Dashboard",
            "Settings",
            "Quit",
        ]:
            box.append(Gtk.Button(label=text))

        popover.set_child(box)
        self.widget.set_popover(popover)