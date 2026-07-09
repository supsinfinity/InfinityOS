from .service import Service


class SettingsService(Service):
    """
    Manages user-configurable application settings.

    Provides centralized access to application preferences
    and broadcasts setting changes to interested components.

    Future responsibilities include theme management,
    preferences, and persistent configuration.
    """

    def __init__(self):
        super().__init__()

        self.settings = {
            "clock_24_hour": False,
            "temperature_unit": "F",
            "animations": True,
        }

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value