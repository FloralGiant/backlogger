# Define Class for Media
class Media:
    """A class to define various sorts of media for backlog"""

    def __init__(self, name, status):
        """Initialize name and status attributes."""
        self.name = name
        self.status = status

        def media_status(self):
            """Return media status in backlog"""
            media_status = f"{self.name} - {self.status}."
            return media_status.title()

# Define Subclass for Books

# Define Subclass for Comics

# Define Subclass for Games