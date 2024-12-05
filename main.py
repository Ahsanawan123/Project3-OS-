from file_operations import create_file, save_file, load_file

if __name__ == "__main__":
    print("Welcome to the File Operations Program!")
    while True:
        print("\nOptions:")
        print("1. Create a file")
        print("2. Save data to a file")
        print("3. Load data from a file")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            filename = input("Enter the file name to create: ").strip()
            create_file(filename)
        elif choice == "2":
            filename = input("Enter the file name to save data to: ").strip()
            data = {}
            while True:
                key = input("Enter a key (or type 'done' to finish): ").strip()
                if key.lower() == 'done':
                    break
                value = input("Enter a value: ").strip()
                data[key] = value
            save_file(filename, data)
        elif choice == "3":
            filename = input("Enter the file name to load data from: ").strip()
            load_file(filename)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
