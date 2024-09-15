"""
Write a program to merge two binary trees. 
Each node in the new tree should hold a value equal 
to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, 
the corresponding node in the new tree should match that input node.
"""

class Node:
    """Binary tree node class"""
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def print_tree(node, level=0, spacing="    "):
    """
    Print the binary tree in a compact format like a traditional tree diagram.
    """
    if node is None:
        return

    # Print the right subtree first (so it's on top in the output)
    if node.right is not None:
        print_tree(node.right, level + 1, spacing)

    # Print the current node with appropriate spacing
    print(spacing * level + str(node.data))

    # Print the left subtree (so it's on the bottom in the output)
    if node.left is not None:
        print_tree(node.left, level + 1, spacing)


def merge(t1: Node, t2: Node):
    """Merges two binary trees using recursion"""

    if t1 is None:
        return t2

    if t2 is None:
        return t1

    merged_node = Node(t1.data + t2.data)
    merged_node.left = merge(t1.left, t2.left)
    merged_node.right = merge(t1.right, t2.right)

    return merged_node

if __name__ == "__main__":

    # Binary tree 1
    root_1 = Node(4)
    root_1.left = Node(5)
    root_1.right = Node(4)
    root_1.left.left = Node(1)
    print("Tree 1")
    print_tree(root_1)

    # binary tree 2
    root_2 = Node(5)
    root_2.left = Node(8)
    root_2.left.left = Node(3)
    print("Tree 2")
    print_tree(root_2)

    # merged tree
    merged_tree = merge(root_1, root_2)
    print("Merged tree")
    print_tree(merged_tree)
