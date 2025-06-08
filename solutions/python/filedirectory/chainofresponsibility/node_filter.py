from abc import ABC, abstractmethod
from typing import Dict, Any

from abstract_node import AbstractNode


class NodeFilter(ABC):
    @abstractmethod
    def apply(self, node: AbstractNode, params: Dict[str, Any]) -> bool:
        """Return True if the node satisfies the filter."""
        pass
