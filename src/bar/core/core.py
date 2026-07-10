from services.service_manager import ServiceManager
from services.weather_service import WeatherService
from services.system_service import SystemService
from core.events.event_bus import EventBus
from services.settings_service import SettingsService
from backends.backend_manager import BackendManager
from backends.system_backend import SystemBackend

class InfinityCore:
    """
    Central infrastructure object for InfinityOS.

    Owns the application's backend architecture, including the
    EventBus, BackendManager, and ServiceManager.

    InfinityCore is responsible for initializing and coordinating
    the application's non-UI systems.

    It does not create or manage GTK widgets.
    """

    def get_event_bus(self):

        """Return the application's Event Bus."""
        
        return self.event_bus

    def __init__(self):

        # Core infrastructure
        self.event_bus = EventBus()

        self.backend_manager = BackendManager()

        self.backend_manager.register(
            SystemBackend()
        )

        system_backend = self.backend_manager.get_backend(
            SystemBackend
        )

        self.service_manager = ServiceManager()

        self.service_manager.register(
            WeatherService(self.event_bus)
        )

        self.service_manager.register(
            SystemService(
                self.event_bus,
                system_backend
    )
)
    
        self.service_manager.register(
            SettingsService()
)

    def get_backend_manager(self):
        return self.backend_manager

    def get_weather_service(self):
        """
        Return the application's WeatherService.
        """

        return self.service_manager.get_service(WeatherService)

    def get_service_manager(self):
        return self.service_manager

    def start(self):
        """Start the application."""
        self.service_manager.start()

    def stop(self):
        """Stop the application."""
        self.service_manager.stop()