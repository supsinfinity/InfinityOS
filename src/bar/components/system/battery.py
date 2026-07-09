from services.system_service import SystemService
from core.events import Events
from components.base import Component

class BatteryComponent(Component):
    """
    Displays the current battery status.

    Refreshes automatically whenever battery information
    changes within the SystemService.
    """
    EVENT = Events.SYSTEM_CHANGED

    def __init__(self, core):
        super().__init__(core)

        self.system_service = self.get_service(
            SystemService
        )

        self.refresh()

    def refresh(self) -> None:
        if not self.system_service:
            self.widget.set_text("BAT --")
            return

        battery = self.system_service.get_battery_percent()

        if battery is None:
            self.widget.set_text("BAT --")
        else:
            self.widget.set_text(f"BAT {battery}%")