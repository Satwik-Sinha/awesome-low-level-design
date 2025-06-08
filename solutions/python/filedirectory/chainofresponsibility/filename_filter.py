import re
from typing import Dict, Any

from abstract_node import AbstractNode
from .node_filter import NodeFilter


class FilenameFilter(NodeFilter):
    """Filter nodes based on a regex applied to their name."""

    def apply(self, node: AbstractNode, params: Dict[str, Any]) -> bool:
        regex = params.get("filenameRegex")
        if not regex:
            return True
        return re.fullmatch(regex, node.get_name()) is not None
