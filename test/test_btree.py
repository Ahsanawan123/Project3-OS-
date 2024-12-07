import sys
import os
sys.path.append("..")

from btree import BTree

def test_btree():
    print("Testing B-Tree Implementation\n")

    filename = "btree_test_file.json"
    if os.path.exists(filename):
        os.remove(filename)

    btree = BTree(t=2, filename=filename)

    keys = [10, 20, 5, 6, 12, 30, 7, 17]
    print("\nInserting keys:", keys)
    for key in keys:
        btree.insert(key, key * 10)
    print("Tree traversal after insertion:")
    traversal_result = btree.traverse()
    print(traversal_result)
    assert traversal_result == sorted([(key, key * 10) for key in keys]), \
        "Error: Traversal does not match expected sorted order."

    print("\nTesting Save and Load:")
    btree.save_to_file()
    print("B-Tree saved successfully.")
    loaded_btree = BTree(t=2, filename=filename)
    loaded_btree.load_from_file()
    print("Traversal after loading:")
    loaded_traversal = loaded_btree.traverse()
    print(loaded_traversal)
    assert traversal_result == loaded_traversal, "Error: B-Tree structure mismatch after loading."

    print("\nAll tests passed successfully!")

if __name__ == "__main__":
    test_btree()
