from typing import Dict, Any

from file_system import FileSystem
from strategy.filename_and_size_search_strategy import FilenameAndSizeSearchStrategy


def main() -> None:
    fs = FileSystem()

    fs.mkdir("/a/b/c")
    fs.add_file("/a/b/c/file1.txt", "Hello")
    fs.add_file("/a/b/c/file2.log", "Data")
    fs.add_file("/a/file3.txt", "Some large content to increase file size...")
    fs.add_file("/a/file4.txt", "Short")

    print("Searching for files and directories matching regex 'file.*\\.txt' with size between 5 and 50 bytes:")

    strategy = FilenameAndSizeSearchStrategy()
    search_params: Dict[str, Any] = {
        "filenameRegex": r"file.*\\.txt",
        "minSize": 5,
        "maxSize": 50,
    }

    found_nodes = fs.search_nodes("/a", strategy, search_params)
    print("Found", len(found_nodes), "nodes")

    for node in found_nodes:
        from file_node import FileNode
        if isinstance(node, FileNode):
            print(f"[FILE] {node.get_name()} (Size: {node.get_size()} bytes)")
        else:
            print(f"[DIR] {node.get_name()}")


if __name__ == "__main__":
    main()
