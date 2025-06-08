from typing import List, Dict, Any

from directory_node import DirectoryNode
from file_node import FileNode
from abstract_node import AbstractNode
from strategy.node_search_strategy import NodeSearchStrategy


class FileSystem:
    def __init__(self) -> None:
        self.root = DirectoryNode("/")

    def _traverse(self, path: str, create_missing_dirs: bool) -> DirectoryNode:
        parts = path.strip("/").split("/")
        current = self.root
        for part in parts:
            if not part:
                continue
            node = current.get_node(part)
            if not isinstance(node, DirectoryNode):
                if create_missing_dirs:
                    node = DirectoryNode(part)
                    current.add_node(node)
                else:
                    return None
            current = node
        return current

    def mkdir(self, path: str) -> None:
        self._traverse(path, True)

    def add_file(self, file_path: str, content: str) -> None:
        parent_path, file_name = file_path.rsplit("/", 1)
        parent = self._traverse(parent_path, True)
        file_node = parent.get_node(file_name)
        if not isinstance(file_node, FileNode):
            file_node = FileNode(file_name)
            parent.add_node(file_node)
        file_node.append_content(content)

    def search_nodes(self, directory_path: str, strategy: NodeSearchStrategy, params: Dict[str, Any]) -> List[AbstractNode]:
        directory = self._traverse(directory_path, False)
        if directory is None:
            raise ValueError(f"Directory not found: {directory_path}")
        return strategy.search(directory, params)
