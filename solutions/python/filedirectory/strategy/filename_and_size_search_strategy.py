from typing import List, Dict, Any

from abstract_node import AbstractNode
from directory_node import DirectoryNode
from chainofresponsibility.filename_filter import FilenameFilter
from chainofresponsibility.file_size_filter import FileSizeFilter
from chainofresponsibility.node_filter_chain import NodeFilterChain
from .node_search_strategy import NodeSearchStrategy


class FilenameAndSizeSearchStrategy(NodeSearchStrategy):
    def __init__(self) -> None:
        self.filter_chain = NodeFilterChain()
        self.filter_chain.add_filter(FilenameFilter())
        self.filter_chain.add_filter(FileSizeFilter())

    def search(self, directory: DirectoryNode, params: Dict[str, Any]) -> List[AbstractNode]:
        result: List[AbstractNode] = []
        self._search_recursive(directory, params, result)
        return result

    def _search_recursive(self, directory: DirectoryNode, params: Dict[str, Any], result: List[AbstractNode]) -> None:
        for node in directory.get_children():
            if self.filter_chain.apply_filters(node, params):
                result.append(node)
            if isinstance(node, DirectoryNode):
                self._search_recursive(node, params, result)
