from abc import ABC, abstractmethod
from typing import List, Dict, Any

from abstract_node import AbstractNode
from directory_node import DirectoryNode


class NodeSearchStrategy(ABC):
    @abstractmethod
    def search(self, directory: DirectoryNode, params: Dict[str, Any]) -> List[AbstractNode]:
        pass
