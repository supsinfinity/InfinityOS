from gi.repository import GLib
from core.logger import  logger
from .service import Service
from core.events.events import Events

class WeatherService(Service):
    """
    Maintains the application's weather state.

    The WeatherService retrieves weather information,
    stores the latest values, and notifies the application
    when weather data changes.

    Weather information is accessed by UI components
    through this service.
    """

    def __init__(self, event_bus):
        super().__init__()

        self.event_bus = event_bus

        self.temperature = "92°F"
        self.condition = "Sunny"

    def get_temperature(self):
        return self.temperature

    def get_condition(self):
        return self.condition

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_condition(self, condition):
        self.condition = condition

    def start(self):
        super().start()

        logger.info("WeatherService started")

        GLib.timeout_add_seconds(5, self._test_update)

    def _test_update(self):
        self.set_temperature("65°F")
        self.set_condition("Cloudy")

        logger.info("Weather data changed.")
        self.event_bus.emit(
            Events.WEATHER_CHANGED
        )
        return True

    def stop(self):
        super().stop()
        logger.info("WeatherService stopped")