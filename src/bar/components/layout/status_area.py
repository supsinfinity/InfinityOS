from gi.repository import Gtk

from components.clock import ClockComponent
from components.information import WeatherComponent
from components.system import CPUComponent
from components.system import MemoryComponent
from components.system import BatteryComponent

class StatusAreaComponent:
    """
    Organizes the right side of the Infinity Bar.
    Owns and arranges system information components
    such as weather, CPU usage, memory usage,
    battery status, and the clock.
    """

    def __init__(self, core):
        self.widget = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=12,
        )

        self.weather = WeatherComponent(core)
        self.cpu = CPUComponent(core)
        self.memory = MemoryComponent(core)
        self.battery = BatteryComponent(core)
        self.clock = ClockComponent()

        self.widget.append(self.weather.widget)
        self.widget.append(self.cpu.widget)
        self.widget.append(self.memory.widget)
        self.widget.append(self.battery.widget)
        self.widget.append(self.clock.widget)