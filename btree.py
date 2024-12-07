import os
from struct import pack, unpack

class Node:
    def __init__(self, t, block_id, is_leaf=True):
        self.t = t
        self.block_id = block_id
        self.is_leaf = is_leaf
        self.keys = []
        self.values = []
        self.children = []

    def is_full(self):
        return len(self.keys) == (2 * self.t - 1)


class BTree:
    HEADER_FORMAT = "8sQQ"
    NODE_FORMAT = "Q Q Q 19Q 19Q 20Q"
    BLOCK_SIZE = 512

    def __init__(self, t, filename):
        self.t = t
        self.filename = filename
        self.root_block_id = 0
        self.next_block_id = 1

        if not os.path.exists(self.filename):
            self._initialize_file()
        else:
            self._read_header()

    def _initialize_file(self):
        magic_number = b"4337PRJ3"
        with open(self.filename, "wb") as f:
            header = pack(self.HEADER_FORMAT, magic_number, self.root_block_id, self.next_block_id)
            f.write(header.ljust(self.BLOCK_SIZE, b"\x00"))

    def _read_header(self):
        with open(self.filename, "rb") as f:
            header = f.read(self.BLOCK_SIZE)
            magic_number, self.root_block_id, self.next_block_id = unpack(self.HEADER_FORMAT, header[:24])
            if magic_number != b"4337PRJ3":
                raise ValueError("Invalid magic number.")

    def _write_header(self):
        with open(self.filename, "r+b") as f:
            header = pack(self.HEADER_FORMAT, b"4337PRJ3", self.root_block_id, self.next_block_id)
            f.write(header.ljust(self.BLOCK_SIZE, b"\x00"))

    def _read_node(self, block_id):
        with open(self.filename, "rb") as f:
            f.seek(block_id * self.BLOCK_SIZE)
            data = f.read(self.BLOCK_SIZE)
            block_id, parent_id, num_keys, *content = unpack(self.NODE_FORMAT, data[:488])
            keys = content[:19]
            values = content[19:38]
            children = content[38:]
            node = Node(self.t, block_id, is_leaf=(children[0] == 0))
            node.keys = [k for k in keys if k != 0]
            node.values = [v for v in values if v != 0]
            node.children = [c for c in children if c != 0]
            return node

    def _write_node(self, node):
        keys = (node.keys + [0] * 19)[:19]
        values = (node.values + [0] * 19)[:19]
        children = (node.children + [0] * 20)[:20]
        
        with open(self.filename, "r+b") as f:
            f.seek(node.block_id * self.BLOCK_SIZE)
            data = pack(self.NODE_FORMAT, node.block_id, 0, len(node.keys), *keys, *values, *children)
            f.write(data.ljust(self.BLOCK_SIZE, b"\x00"))

    def insert(self, key, value):
        if self.search(key):  # Check for duplicate keys
            return False  # Reject duplicates
        if self.root_block_id == 0:
            root = Node(self.t, self.next_block_id)
            self.root_block_id = self.next_block_id
            self.next_block_id += 1
            self._write_node(root)
        root = self._read_node(self.root_block_id)
        if root.is_full():
            new_root = Node(self.t, self.next_block_id, is_leaf=False)
            self.next_block_id += 1
            new_root.children.append(root.block_id)
            self._split_child(new_root, 0, root)
            self.root_block_id = new_root.block_id
            self._write_node(new_root)
        self._insert_non_full(self._read_node(self.root_block_id), key, value)
        self._write_header()
        return True

    def _insert_non_full(self, node, key, value):
        idx = len(node.keys) - 1
        if node.is_leaf:
            while idx >= 0 and key < node.keys[idx]:
                idx -= 1
            node.keys.insert(idx + 1, key)
            node.values.insert(idx + 1, value)
            self._write_node(node)
        else:
            while idx >= 0 and key < node.keys[idx]:
                idx -= 1
            idx += 1
            child = self._read_node(node.children[idx])
            if child.is_full():
                self._split_child(node, idx, child)
                if key > node.keys[idx]:
                    idx += 1
            self._insert_non_full(self._read_node(node.children[idx]), key, value)

    def _split_child(self, parent, idx, child):
        t = self.t
        new_node = Node(self.t, self.next_block_id, is_leaf=child.is_leaf)
        self.next_block_id += 1
        parent.keys.insert(idx, child.keys[t - 1])
        parent.values.insert(idx, child.values[t - 1])
        parent.children.insert(idx + 1, new_node.block_id)
        new_node.keys = child.keys[t:]
        new_node.values = child.values[t:]
        child.keys = child.keys[:t - 1]
        child.values = child.values[:t - 1]
        if not child.is_leaf:
            new_node.children = child.children[t:]
            child.children = child.children[:t]
        self._write_node(child)
        self._write_node(new_node)
        self._write_node(parent)

    def traverse(self):
        def _traverse(node):
            for i in range(len(node.keys)):
                if not node.is_leaf:
                    _traverse(self._read_node(node.children[i]))
                result.append((node.keys[i], node.values[i]))
            if not node.is_leaf:
                _traverse(self._read_node(node.children[-1]))

        self._read_header()
        result = []
        if self.root_block_id != 0:
            root = self._read_node(self.root_block_id)
            _traverse(root)
        return result

    def search(self, key):
        def _search(node, key):
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if i < len(node.keys) and key == node.keys[i]:
                return node.values[i]
            if node.is_leaf:
                return None
            child = self._read_node(node.children[i])
            return _search(child, key)

        if self.root_block_id == 0:
            return None  # Empty tree
        root = self._read_node(self.root_block_id)
        return _search(root, key)

    def load_from_file(self, load_file_name):
        with open(load_file_name, "r") as file:
            for line in file:
                try:
                    key, value = map(int, line.strip().split(","))
                    self.insert(key, value)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")

    def extract_to_file(self, output_file):
        if os.path.exists(output_file):
            overwrite = input(f"File {output_file} already exists. Overwrite? (yes/no): ").strip().lower()
            if overwrite != "yes":
                print("Operation aborted.")
                return

        with open(output_file, "w") as file:
            for key, value in self.traverse():
                file.write(f"{key},{value}\n")
