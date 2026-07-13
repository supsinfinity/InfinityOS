class Context:
    """
    represents a single piece of information that 
    may be displayed by the Context Engine.
    """

    title: str
    priority: int
    icon: str | None
    provider: str

class ContextProvider:
    """
    Base class for all Context providers.
    """