from typing import Dict, List

from abstract_node import AbstractNode


class DirectoryNode(AbstractNode):
    """Represents a directory containing child nodes."""

    def __init__(self, name: str):
        super().__init__(name)
        self.children: Dict[str, AbstractNode] = {}

    def add_node(self, node: AbstractNode) -> None:
        self.children[node.get_name()] = node

    def get_children(self) -> List[AbstractNode]:
        return list(self.children.values())

    def get_node(self, name: str) -> AbstractNode:
        return self.children.get(name)
