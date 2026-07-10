from components.base import Component
from services.system_service import SystemService
from core.events.events import Events

class MemoryComponent(Component):
    """
    Displays current memory usage./
    Refreshes automatically when system information changes.
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
            used = self.system_service.get_memory_used()
            total = self.system_service.get_memory_total()
            self.widget.set_text(
            f"MEM {used:.1f} GB"
            )
        else:
            self.widget.set_text("MEM --")