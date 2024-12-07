import os

def create_corrupted_file(filename):
    """Creates a corrupted file by writing an invalid magic number."""
    # Ensure file is created in the parent directory
    parent_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
    file_path = os.path.join(parent_dir, filename)  # Combine with filename

    with open(file_path, "wb") as f:
        f.write(b"INVALID1")  # Invalid magic number
        f.write(b"\x00" * 504)  # Fill the rest of the header with zeros
    print(f"Corrupted file '{file_path}' created.")

def create_invalid_load_file(filename):
    """Creates a file with invalid data for testing the load command."""
    # Ensure file is created in the parent directory
    parent_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
    file_path = os.path.join(parent_dir, filename)  # Combine with filename

    with open(file_path, "w") as f:
        f.write("10,abc\n")         # Invalid value
        f.write("20\n")            # Missing value
        f.write("hello,world\n")   # Completely invalid format
        f.write("30,300\n")        # Valid line
    print(f"Invalid load file '{file_path}' created.")

if __name__ == "__main__":
    create_corrupted_file("corrupted_file.btree")
    create_invalid_load_file("invalid_load.txt")
