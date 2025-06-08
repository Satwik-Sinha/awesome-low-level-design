from typing import Dict, Any

from abstract_node import AbstractNode
from file_node import FileNode
from .node_filter import NodeFilter


class FileSizeFilter(NodeFilter):
    """Filter FileNode objects based on size range."""

    def apply(self, node: AbstractNode, params: Dict[str, Any]) -> bool:
        if not isinstance(node, FileNode):
            return True
        min_size = params.get("minSize")
        max_size = params.get("maxSize")
        if min_size is None or max_size is None:
            return True
        size = node.get_size()
        return min_size <= size <= max_size
