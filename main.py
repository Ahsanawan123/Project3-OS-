from file_operations import create_file, save_file
from btree import BTree
import os

def main():
    btree = None
    filename = None

    print("Welcome to the B-Tree Index Manager!")
    while True:
        print("\nCommands: CREATE, OPEN, INSERT, SEARCH, LOAD, PRINT, EXTRACT, QUIT")
        command = input("Enter a command: ").strip().lower()

        if command == "create":
            filename = input("Enter the name of the file to create: ").strip()
            create_file(filename)
            try:
                btree = BTree(t=10, filename=filename)
                print(f"File '{filename}' created and opened.")
            except Exception as e:
                print(f"Error opening the created file: {e}")

        elif command == "open":
            filename = input("Enter the name of the file to open: ").strip()
            if not os.path.exists(filename):
                print(f"Error: File '{filename}' does not exist.")
                continue
            try:
                btree = BTree(t=10, filename=filename)
                print(f"File '{filename}' opened successfully.")
            except Exception as e:
                print(f"Error opening file: {e}")

        elif command == "insert":
            if btree is None:
                print("No file is open. Use CREATE or OPEN to start.")
                continue
            try:
                key = int(input("Enter the key: ").strip())
                value = int(input("Enter the value: ").strip())
                if btree.insert(key, value):  # Handle duplicate key rejection
                    print(f"Inserted key-value pair: ({key}, {value}).")
                else:
                    print(f"Error: Key {key} already exists.")
            except ValueError:
                print("Invalid input. Key and Value must be integers.")

        elif command == "search":
            if btree is None:
                print("No file is open. Use CREATE or OPEN to start.")
                continue
            try:
                key = int(input("Enter the key to search: ").strip())
                result = btree.search(key)
                if result is not None:
                    print(f"Key {key} found with value: {result}")
                else:
                    print(f"Key {key} not found.")
            except ValueError:
                print("Invalid input. Key must be an integer.")

        elif command == "load":
            if btree is None:
                print("No file is open. Use CREATE or OPEN to start.")
                continue
            try:
                load_file_name = input("Enter the name of the file to load from: ").strip()
                btree.load_from_file(load_file_name)
                print(f"Data from '{load_file_name}' loaded successfully into the index.")
            except Exception as e:
                print(f"Error loading file: {e}")

        elif command == "print":
            if btree is None:
                print("No file is open. Use CREATE or OPEN to start.")
                continue
            print("Tree traversal (keys and values):", btree.traverse())

        elif command == "extract":
            if btree is None:
                print("No file is open. Use CREATE or OPEN to start.")
                continue
            try:
                output_file = input("Enter the name of the file to extract to: ").strip()
                btree.extract_to_file(output_file)
                print(f"Data successfully extracted to '{output_file}'.")
            except Exception as e:
                print(f"Error during extraction: {e}")

        elif command == "quit":
            print("Exiting the B-Tree Index Manager. Goodbye!")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
