# prompt: build BST from sorted array and also print with example

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sorted_array_to_bst(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = Node(arr[mid])

    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])

    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7]
root = sorted_array_to_bst(sorted_array)

print("Inorder traversal of the constructed BST:")
inorder_traversal(root)
print()
