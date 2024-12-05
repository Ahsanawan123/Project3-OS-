import os

def create_file(filename):
    """Creates a new file or overwrites an existing one after confirmation."""
    if os.path.exists(filename):
        overwrite = input(f"File {filename} exists. Overwrite? (yes/no): ").strip().lower()
        if overwrite != 'yes':
            print("Operation aborted.")
            return
    try:
        with open(filename, 'w') as f:
            f.write("")  # Create an empty file
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

def save_file(filename, data):
    """Saves data (a dictionary) to the specified file."""
    try:
        with open(filename, 'w') as f:
            for key, value in data.items():
                f.write(f"{key},{value}\n")  # Save as CSV-like format
        print(f"Data saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_file(filename):
    """Loads data from the specified file and returns it as a dictionary."""
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return None
    try:
        data = {}
        with open(filename, 'r') as f:
            for line in f:
                key, value = line.strip().split(',')
                data[key] = value
        print(f"Data loaded from '{filename}': {data}")
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
