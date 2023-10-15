package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// define a class for a segment tree
type SegmentTree struct {
	n int
	a []int
}

// initialize a segment tree
func NewSegmentTree(n int) *SegmentTree {
	return &SegmentTree{
		n: n,
		a: make([]int, 4*n),
	}
}

// build a segment tree
func (st *SegmentTree) Build(a []int, node, start, end int) int {
	if start == end {
		st.a[node] = a[start]
		return st.a[node]
	}

	mid := (start + end) / 2
	st.a[node] = st.Build(a, node*2, start, mid) + st.Build(a, node*2+1, mid+1, end)
	return st.a[node]
}

// update a segment tree
func (st *SegmentTree) Update(node, start, end, index, value int) {
	if index < start || index > end {
		return
	}

	if start == end {
		st.a[node] = value
	} else {
		mid := (start + end) / 2
		st.Update(node*2, start, mid, index, value)
		st.Update(node*2+1, mid+1, end, index, value)
		st.a[node] = st.a[node*2] + st.a[node*2+1]
	}
}

// query a segment tree
func (st *SegmentTree) Query(node, start, end, left, right int) int {
	if left > end || right < start {
		return 0
	}

	if left <= start && end <= right {
		return st.a[node]
	}

	mid := (start + end) / 2
	return st.Query(node*2, start, mid, left, right) + st.Query(node*2+1, mid+1, end, left, right)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m int
	var a []int
	fmt.Fscan(in, &n)
	a = make([]int, n+1)
	for i := 1; i <= n; i++ {
		fmt.Fscan(in, &a[i])
	}

	changeQueries := make([][2]int, 0)
	sumQueries := make([][4]int, 0)
	sumQueryCount := 0
	fmt.Fscan(in, &m)
	for l := 0; l < m; l++ {
		var q int
		fmt.Fscan(in, &q)
		if q == 1 {
			var i, v int
			fmt.Fscan(in, &i, &v)
			changeQueries = append(changeQueries, [2]int{i, v})
		} else {
			var k, i, j int
			fmt.Fscan(in, &k, &i, &j)
			sumQueries = append(sumQueries, [4]int{k, i, j, sumQueryCount})
			sumQueryCount++
		}
	}

	st := NewSegmentTree(n)
	st.Build(a, 1, 1, n)

	sort.Slice(sumQueries, func(i, j int) bool {
		return sumQueries[i][0] < sumQueries[j][0]
	})

	answer := make([]int, sumQueryCount)
	l := 0
	for _, sumQuery := range sumQueries {
		k, i, j := sumQuery[0], sumQuery[1], sumQuery[2]
		for ; l < k; l++ {
			changeQuery := changeQueries[l]
			st.Update(1, 1, n, changeQuery[0], changeQuery[1])
		}
		answer[sumQuery[3]] = st.Query(1, 1, n, i, j)
	}

	for _, v := range answer {
		fmt.Fprintln(out, v)
	}
}
