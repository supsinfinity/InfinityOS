from components.base import Component

from services.weather_service import WeatherService

from core.events.events import Events


class WeatherComponent(Component):
    """
    Displays the current weather information.

    Listens for weather update events and refreshes
    its display whenever the WeatherService reports
    new data.
    """

    EVENT = Events.WEATHER_CHANGED

    def __init__(self, core):
        super().__init__(core)

        self.weather_service = self.get_service(
            WeatherService
        )

        self.refresh()

    def refresh(self) -> None:
        if self.weather_service:
            self.widget.set_text(
                f"{self.weather_service.get_temperature()} • "
                f"{self.weather_service.get_condition()}"
            )
        else:
            self.widget.set_text("--")