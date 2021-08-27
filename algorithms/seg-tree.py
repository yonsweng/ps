class SegTree:
    def __init__(self, data):
        self.data = data
        self.tree = [0] * (4 * len(self.data))

        self.init(1, 0, len(self.data) - 1)

    def init(self, index, tree_left, tree_right):
        if tree_left == tree_right:
            self.tree[index] = self.data[tree_left]
            return self.tree[index]

        self.tree[index] = self.init(index * 2, tree_left, (tree_left + tree_right) // 2) \
            + self.init(index * 2 + 1, (tree_left + tree_right) // 2 + 1, tree_right)

        return self.tree[index]

    def __update__(self, index, data_index, element, tree_left, tree_right):
        if tree_left == tree_right:
            self.tree[index] = element
            return self.tree[index]

        if data_index < tree_left or tree_right < data_index:
            return self.tree[index]

        self.tree[index] = \
            self.__update__(index * 2, data_index, element, tree_left, (tree_left + tree_right) // 2) + \
            self.__update__(index * 2 + 1, data_index, element, (tree_left + tree_right) // 2 + 1, tree_right)

        return self.tree[index]

    def __query__(self, index, query_left, query_right, tree_left, tree_right):
        if query_left <= tree_left and tree_right <= query_right:
            return self.tree[index]

        if tree_right < query_left or query_right < tree_left:
            return 0

        return self.__query__(index * 2, query_left, query_right, tree_left, (tree_left + tree_right) // 2) + \
            self.__query__(index * 2 + 1, query_left, query_right, (tree_left + tree_right) // 2 + 1, tree_right)

    def update(self, data_index, element):
        self.__update__(1, data_index, element, 0, len(self.data) - 1)
    
    def query(self, left, right):
        return self.__query__(1, left, right, 0, len(self.data) - 1)


def main():
    st = SegTree([1, 2, 3, 4, 5, 6, 7, 8, 9])

    print(st.query(4, 8))
    st.update(2, 1)
    print(st.query(2, 3))


if __name__ == '__main__':
    main()
