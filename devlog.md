## [Date: Dec 2, 2024, 5:00 PM]
### Changes:
- Set up local Git repository on Windows.
- Linked local Git repository to GitHub.
- Verified GitHub integration by pushing and pulling changes.
- Set up `cs1` environment to pull updates from the GitHub repository.
- Tested syncing files between local, GitHub, and `cs1`.

### Next Steps:
- Start implementing file operations (`create_file`, `save_file`, `load_file`).
- Test basic file creation locally and on `cs1`.

## [Date: Dec 2, 2024, 7:00 PM]
### Changes:
- Implemented `create_file`, `save_file`, and `load_file` functions in `file_operations.py`.
- Created `test/test_file_operations.py` to test file operations.
- Successfully tested file operations (`create`, `save`, `load`) locally and on `cs1`.
- Removed `test_file.txt` from the repository and updated `.gitignore` to exclude it from future commits.
- Confirmed removal of `test_file.txt` on GitHub and synced changes with `cs1`.

### Next Steps:
- Begin planning and implementing the B-Tree structure in a new file (`btree.py`).
- Define B-Tree node structure and start working on the `insert` function.
