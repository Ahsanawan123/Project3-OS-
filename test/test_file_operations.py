import sys
import os

# Add the parent directory of the current file to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from file_operations import create_file, save_file, load_file

def test_file_operations():
    filename = "test_file.txt"

    # Test file creation
    print("\nTesting create_file()...")
    create_file(filename)

    # Test saving data
    print("\nTesting save_file()...")
    sample_data = {"key1": "value1", "key2": "value2", "key3": "value3"}
    save_file(filename, sample_data)

    # Test loading data
    print("\nTesting load_file()...")
    loaded_data = load_file(filename)
    assert loaded_data == sample_data, "Loaded data does not match saved data."

    print("\nAll tests passed successfully!")

if __name__ == "__main__":
    test_file_operations()
