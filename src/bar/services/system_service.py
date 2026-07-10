from gi.repository import GLib

from .service import Service

from core.events import Events

from backends.system_backend import SystemBackend

from core.logger import logger

class SystemService(Service):
    """
    Maintains general system information.

    The SystemService retrieves CPU, memory, battery,
    and other system statistics through registered backends.

    Whenever system information changes, the service
    notifies interested components through the EventBus.
    """

    def __init__(self, event_bus, backend):
        super().__init__()

        self.event_bus = event_bus
        self.backend = backend

        self.cpu_usage = 0.0
        self.memory_used = 0.0
        self.memory_total = 0.0
        self.battery_percent = None

    def get_cpu_usage(self) -> float:
        return self.cpu_usage
    
    def get_memory_total(self):
        return self.memory_total
    
    def get_memory_used(self) -> float:
        return self.memory_used
    
    def get_battery_percent(self):
        return self.battery_percent

    def start(self):
        super().start()

        logger.info("SystemService started")

        GLib.timeout_add_seconds(
            2,
            self._update
        )

    def _update(self):
        self.cpu_usage = self.backend.get_cpu_usage()

        memory = self.backend.get_memory()
        self.memory_used = memory.used / (1024 ** 3)
        self.memory_total = memory.total / (1024 ** 3)

        self.battery_percent = self.backend.get_battery_percent()

        logger.debug(
            f"CPU: {self.cpu_usage:.0f}% | "
            f"Memory: {self.memory_used:.1f}/{self.memory_total:.1f} GB | "
            f"Battery: {self.battery_percent:.0f}%"
    )

        self.event_bus.emit(Events.SYSTEM_CHANGED)

        return True

    def stop(self):
        super().stop()

        logger.info("SystemService stopped")