
class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf


class BTree:
    def __init__(self, order):
        self.root = BTreeNode(leaf=True)
        self.order = order

    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return True

        if node.leaf:
            return False

        return self.search(node.children[i], key)

    def split_child(self, parent, i):
        order = self.order
        child = parent.children[i]
        new_node = BTreeNode(leaf=child.leaf)

        mid = (order - 1) // 2
        median = child.keys[mid]

        new_node.keys = child.keys[mid + 1:]
        child.keys = child.keys[:mid]

        if not child.leaf:
            new_node.children = child.children[mid + 1:]
            child.children = child.children[:mid + 1]

        parent.children.insert(i + 1, new_node)
        parent.keys.insert(i, median)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append(0)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key

        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            if len(node.children[i].keys) == self.order - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1

            self.insert_non_full(node.children[i], key)

    def insert(self, key):
        root = self.root

        if len(root.keys) == self.order - 1:
            new_root = BTreeNode()
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root

        self.insert_non_full(self.root, key)

    def display(self, node=None, level=0):
        if node is None:
            node = self.root

        print("Level", level, ":", node.keys)

        for child in node.children:
            self.display(child, level + 1)


# Main program
order = int(input("Enter B-Tree order: "))
tree = BTree(order)

n = int(input("Enter number of keys: "))
keys = list(map(int, input("Enter keys separated by spaces: ").split()))

if len(keys) != n:
    print("Error: Number of keys does not match.")
else:
    for key in keys:
        tree.insert(key)

    print("\nB-Tree structure:")
    tree.display()

    search_key = int(input("\nEnter key to search: "))
    if tree.search(tree.root, search_key):
        print(search_key, "found in B-Tree")
    else:
        print(search_key, "not found in B-Tree")
