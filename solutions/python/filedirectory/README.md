# Designing a File Directory System

This example demonstrates a simple file directory structure that supports searching using the Strategy and Chain of Responsibility patterns.

## Key Classes
* **AbstractNode** – base class for files and directories.
* **FileNode** – represents a file and stores its content and size.
* **DirectoryNode** – container that can hold files and sub‑directories.
* **FileSystem** – provides APIs to create directories, add files and search.
* **NodeFilter** / **NodeFilterChain** – filters used in the search process.
* **FilenameAndSizeSearchStrategy** – strategy that searches based on filename and size constraints.

Run `file_system_demo.py` to see a small demo.
