from typing import List, Dict, Any

from abstract_node import AbstractNode
from .node_filter import NodeFilter


class NodeFilterChain:
    """Chain of responsibility to apply multiple filters."""

    def __init__(self) -> None:
        self.filters: List[NodeFilter] = []

    def add_filter(self, node_filter: NodeFilter) -> None:
        self.filters.append(node_filter)

    def apply_filters(self, node: AbstractNode, params: Dict[str, Any]) -> bool:
        for f in self.filters:
            if not f.apply(node, params):
                return False
        return True
