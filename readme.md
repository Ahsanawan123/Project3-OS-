## B-Tree Index Manager

### Overview
This project implements a **B-Tree-based index manager** for efficient key-value operations such as insertion, searching, and traversal. It also provides functionality for saving and loading index files, handling invalid/corrupted files, and extracting data to external files.  

The program is designed to run on both **Windows** (via Git Bash) and **cs1** (UTD's server environment).  

## Getting Started

### Local Copy Already Available?
If you already have the project files locally, **skip the GitHub cloning step** and proceed to [Navigating the Project](#navigating-the-project).

### Cloning from GitHub

#### Windows/CS1 (UTD Server):
To clone the project, use the following command in **Git Bash** or your terminal:  
```bash
git clone https://github.com/Ahsanawan123/Project3-OS-.git
```
## Navigating the Project

### Windows/cs1 (UTD Server)
- Open the project folder in your terminal:
```bash
cd Navigate/to/Project/location/Project3-OS-
```
## Running the program
### Windows:
- Run the program using the following command in Git Bash:
```bash
python main.py
```
### CS1 (UTD Server): 
- Use the following command to run the program:
```bash
python3 main.py
```
## Available Commands
- The B-Tree Index Manager supports the following commands:

| Command   | Description                                                                                     |
|-----------|-------------------------------------------------------------------------------------------------|
| CREATE    | Create a new index file and open it. If the file exists, you'll be prompted to overwrite it.    |
| OPEN      | Open an existing index file. If the file doesn't exist or is corrupted, an error is shown.      |
| INSERT    | Insert a key-value pair into the index. If the key already exists, it will be rejected.         |
| SEARCH    | Search for a key in the index. If found, the value is displayed; otherwise, an error message.   |
| LOAD      | Load a file of key-value pairs into the index (e.g., `key,value` format).                       |
| PRINT     | Print all key-value pairs in the index in sorted order.                                         |
| EXTRACT   | Export all key-value pairs in the index to a file in `key,value` format.                        |
| QUIT      | Exit the program.                                                                               |

## Example Scenarios
1.) create a New file:
```bash
Enter a command: create
Enter the name of the file to create: index1
File 'index1' created successfully.
```
2.) Insert Key - Value Pairs:
```bash
Enter a command: insert
Enter the key: 10
Enter the value: 100
Inserted key-value pair: (10, 100).
```
3.) Search for a Key:
```bash
Enter a command: search
Enter the key to search: 10
Key 10 found with value: 100
```
4.) Load Data from a file:
```bash
Enter a command: load
Enter the name of the file to load from: loadfile.txt
Data from 'loadfile.txt' loaded successfully into the index.
```
5.) Print All Data:
```bash
Enter a command: print
Tree traversal (keys and values): [(10, 100), (15, 150), (20, 200)]
```
6.) Export Data:
```bash
Enter a command: extract
Enter the name of the file to extract to: output.txt
Data successfully extracted to 'output.txt'.
```

## File Explanations
- **btree.py:** Contains the B-Tree implementation, including key insertion, search, and traversal logic.
- **main.py:** The main driver program providing the command-line interface.
- **file_operations.py:** Handles file creation, saving, and loading operations.
- **test/test_btree.py:** Unit tests for the B-Tree functionality.
- **test/test_file_operations.py:** Unit tests for file operation functions.
- **corrupt-invalid_file_generator.py:** Generates corrupted and invalid files for testing purposes.

## Running Tests
1.) Navigate to the test/ directory:
```bash
cd test
```
2.) Run the desired test file:
- For B-Tree Tests:
```bash
python test_btree.py
```
- For File Operation Tests:
```bash
python test_file_operations.py
```
- For corrupted and invalid file Tests:
```bash
python corrupt-invalid_file_genererator.py
```
3.) View test results directly in the terminal.

## Note for CS1 Enviroments
- Use python3 instead of python for running the program or tests.
- Ensure your cloned repository is in the correct working directory under projects/.