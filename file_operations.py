import os
from struct import pack

def create_file(filename):
    """Creates a new index file with a valid B-Tree header."""
    if os.path.exists(filename):
        overwrite = input(f"File {filename} already exists. Overwrite? (yes/no): ").strip().lower()
        if overwrite != 'yes':
            print("Operation aborted.")
            return
    try:
        # B-Tree file header initialization
        magic_number = b"4337PRJ3"  # Identifier for the B-Tree file
        root_block_id = 0
        next_block_id = 1
        header_format = "8sQQ"
        block_size = 512

        with open(filename, 'wb') as f:
            # Write a valid B-Tree header
            header = pack(header_format, magic_number, root_block_id, next_block_id)
            f.write(header.ljust(block_size, b"\x00"))  # Pad the header to block size
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")


def save_file(filename, btree):
    """Saves the entire B-Tree to the file."""
    try:
        btree.save_to_file()
        print(f"B-Tree saved to '{filename}' successfully.")
    except Exception as e:
        print(f"Error saving B-Tree to file: {e}")


def load_file(filename, t=10):
    """Loads a B-Tree from a file."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        return None
    try:
        from btree import BTree
        btree = BTree(t, filename)
        btree.load_from_file()
        print(f"B-Tree loaded from '{filename}' successfully.")
        return btree
    except Exception as e:
        print(f"Error loading B-Tree from file: {e}")
        return None
