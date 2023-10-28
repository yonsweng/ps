package main

import (
	"bufio"
	"fmt"
	"os"
)

type SegmentTree struct {
	tree   []int
	lazy   []int
	length int
}

func (st *SegmentTree) init(n int) {
	st.length = n
	st.tree = make([]int, n*4)
	st.lazy = make([]int, n*4)
}

func (st *SegmentTree) propagate(node, start, end int) {
	if st.lazy[node] != 0 {
		st.tree[node] = (end - start + 1) - st.tree[node]
		if start != end {
			st.lazy[node*2] ^= 1
			st.lazy[node*2+1] ^= 1
		}
		st.lazy[node] = 0
	}
}

func (st *SegmentTree) update(node, start, end, left, right int) {
	st.propagate(node, start, end)
	if end < left || right < start {
		return
	}
	if left <= start && end <= right {
		st.tree[node] = (end - start + 1) - st.tree[node]
		if start != end {
			st.lazy[node*2] ^= 1
			st.lazy[node*2+1] ^= 1
		}
		return
	}
	mid := (start + end) / 2
	st.update(node*2, start, mid, left, right)
	st.update(node*2+1, mid+1, end, left, right)
	st.tree[node] = st.tree[node*2] + st.tree[node*2+1]
}

func (st *SegmentTree) query(node, start, end, left, right int) int {
	st.propagate(node, start, end)
	if end < left || right < start {
		return 0
	}
	if left <= start && end <= right {
		return st.tree[node]
	}
	mid := (start + end) / 2
	return st.query(node*2, start, mid, left, right) + st.query(node*2+1, mid+1, end, left, right)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, m int
	fmt.Fscanln(reader, &n, &m)

	st := SegmentTree{}
	st.init(n)

	for i := 0; i < m; i++ {
		var cmd, left, right int
		fmt.Fscanln(reader, &cmd, &left, &right)
		if cmd == 0 {
			st.update(1, 1, n, left, right)
		} else {
			fmt.Fprintln(writer, st.query(1, 1, n, left, right))
		}
	}
}
