package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type SegmentTree struct {
	tree     []int
	funcType string
	e        int
}

func NewSegmentTree(n int, arr []int, funcType string, e int) *SegmentTree {
	st := &SegmentTree{
		tree:     make([]int, 4*n),
		funcType: funcType,
		e:        e,
	}
	st.init(1, 0, n-1, arr)
	return st
}

func (st *SegmentTree) init(node, start, end int, arr []int) int {
	if start == end {
		st.tree[node] = arr[start]
		return st.tree[node]
	}
	mid := (start + end) / 2
	left := st.init(node*2, start, mid, arr)
	right := st.init(node*2+1, mid+1, end, arr)
	st.tree[node] = st.compute(left, right)
	return st.tree[node]
}

func (st *SegmentTree) compute(left, right int) int {
	if st.funcType == "max" {
		if left > right {
			return left
		}
		return right
	} else {
		if left < right {
			return left
		}
		return right
	}
}

func (st *SegmentTree) update(node, start, end, index, value int) int {
	if index < start || index > end {
		return st.tree[node]
	}
	if start == end {
		st.tree[node] = value
		return st.tree[node]
	}
	mid := (start + end) / 2
	left := st.update(node*2, start, mid, index, value)
	right := st.update(node*2+1, mid+1, end, index, value)
	st.tree[node] = st.compute(left, right)
	return st.tree[node]
}

func (st *SegmentTree) query(node, start, end, left, right int) int {
	if left > end || right < start {
		return st.e
	}
	if left <= start && end <= right {
		return st.tree[node]
	}
	mid := (start + end) / 2
	l := st.query(node*2, start, mid, left, right)
	r := st.query(node*2+1, mid+1, end, left, right)
	return st.compute(l, r)
}

func solution() {
	reader := bufio.NewReader(os.Stdin)
	tStr, _ := reader.ReadString('\n')
	t, _ := strconv.Atoi(strings.TrimSpace(tStr))
	for i := 0; i < t; i++ {
		line, _ := reader.ReadString('\n')
		parts := strings.Fields(line)
		n, _ := strconv.Atoi(parts[0])
		k, _ := strconv.Atoi(parts[1])

		dvds := make([]int, n)
		for i := range dvds {
			dvds[i] = i
		}

		maxTree := NewSegmentTree(n, dvds, "max", 0)
		minTree := NewSegmentTree(n, dvds, "min", 100000)

		for j := 0; j < k; j++ {
			query, _ := reader.ReadString('\n')
			qParts := strings.Fields(query)
			q, _ := strconv.Atoi(qParts[0])
			a, _ := strconv.Atoi(qParts[1])
			b, _ := strconv.Atoi(qParts[2])

			if q == 0 {
				maxTree.update(1, 0, n-1, a, dvds[b])
				maxTree.update(1, 0, n-1, b, dvds[a])
				minTree.update(1, 0, n-1, a, dvds[b])
				minTree.update(1, 0, n-1, b, dvds[a])
				dvds[a], dvds[b] = dvds[b], dvds[a]
			} else {
				minValue := minTree.query(1, 0, n-1, a, b)
				maxValue := maxTree.query(1, 0, n-1, a, b)
				if minValue == a && maxValue == b {
					fmt.Println("YES")
				} else {
					fmt.Println("NO")
				}
			}
		}
	}
}

func main() {
	solution()
}
