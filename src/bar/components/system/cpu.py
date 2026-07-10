from components.base import Component

from services.system_service import SystemService

from core.events.events import Events


class CPUComponent(Component):
    """
    Displays the current CPU utilization.

    Automatically refreshes whenever the SystemService
    publishes updated system information.
    """

    EVENT = Events.SYSTEM_CHANGED

    def __init__(self, core):
        super().__init__(core)

        self.system_service = self.get_service(
            SystemService
        )

        self.refresh()

    def refresh(self) -> None:
        if self.system_service:
            self.widget.set_text(
                f"CPU {self.system_service.get_cpu_usage():.0f}%"
            )
        else:
            self.widget.set_text("CPU --")