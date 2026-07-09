from .weather_service import WeatherService
from .system_service import SystemService

class ServiceManager:
    """
    Manages the lifecycle of all application services.

    Services are responsible for application logic and own
    the application's state.

    The ServiceManager registers, starts, stops, and provides
    access to services throughout the application.
    """

    def __init__(self):
        self.services = []

    def register(self, service):
        #Register a service with the manager.
        self.services.append(service)

    def get_service(self, service_type):
        """
        Return the first registered service of the requested type.
        """
        for service in self.services:
            if isinstance(service, service_type):
                return service

        return None

    def start(self):
        """Start all services."""
        for service in self.services:
            service.start()

    def stop(self):
        """Stop all services."""
        for service in self.services:
            service.stop()