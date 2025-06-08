from abstract_node import AbstractNode


class FileNode(AbstractNode):
    """Represents a file with content and size."""

    def __init__(self, name: str):
        super().__init__(name)
        self.content = ""
        self.size = 0

    def append_content(self, new_content: str) -> None:
        self.content += new_content
        self.size += len(new_content)

    def read_content(self) -> str:
        return self.content

    def get_size(self) -> int:
        return self.size
