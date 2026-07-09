import psutil
from .backend import Backend

class SystemBackend(Backend):
    """
    Provides access to operating system statistics.

    Retrieves information such as CPU usage, memory usage,
    battery status, and other hardware metrics.

    This backend contains no application logic.
    """

    def get_cpu_usage(self) -> float:
        return psutil.cpu_percent(interval=None)
    
    def get_memory_usage(self):
        """
        Return the current memory usage percentage.
        """
        return psutil.virtual_memory().percent
    
    def get_battery_percent(self):
        """
        Return the battery percentage, or None if unavailable.
        """
        battery = psutil.sensors_battery()

        if battery is None:
            return None

        return battery.percent