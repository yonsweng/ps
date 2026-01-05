from sys import stdin


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []


def solve():
    while True:
        n, k = map(int, stdin.readline().strip().split())
        if n == 0 and k == 0:
            break

        seq = list(map(int, stdin.readline().strip().split()))

        root = TreeNode(seq[0])
        nodes, first_leaf = [root], -1
        for i in range(1, n):
            node = TreeNode(seq[i])
            if seq[i - 1] + 1 == seq[i]:
                nodes[first_leaf].children.append(node)
                node.parent = nodes[first_leaf]
            else:
                first_leaf += 1
                nodes[first_leaf].children.append(node)
                node.parent = nodes[first_leaf]
            nodes.append(node)

        # Find the node with value k
        target_node = None
        for node in nodes:
            if node.value == k:
                target_node = node
                break

        # Find the number of cousins
        if (
            target_node is None
            or target_node.parent is None
            or target_node.parent.parent is None
        ):
            print(0)
            continue

        grandparent = target_node.parent.parent
        cousin_count = 0
        for sibling in grandparent.children:
            if sibling != target_node.parent:
                cousin_count += len(sibling.children)

        print(cousin_count)


if __name__ == "__main__":
    solve()
