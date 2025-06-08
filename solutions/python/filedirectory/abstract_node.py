from datetime import datetime


class AbstractNode:
    """Base class for files and directories."""

    def __init__(self, name: str):
        self.name = name
        self.created_at = datetime.now()

    def get_name(self) -> str:
        return self.name

    def get_created_at(self) -> datetime:
        return self.created_at
