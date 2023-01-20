package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type treeNode struct {
	e    []int
	l, r int
}

type mergeSortTree struct {
	n     int
	nodes []treeNode
}

func (t *mergeSortTree) merge(i, l, r int, e []int) {
	if l == r {
		t.nodes[i].e = append(t.nodes[i].e, e[l])
		return
	}

	m := (l + r) / 2
	t.merge(i*2, l, m, e)
	t.merge(i*2+1, m+1, r, e)

	for p, q := 0, 0; p < len(t.nodes[i*2].e) || q < len(t.nodes[i*2+1].e); {
		if q == len(t.nodes[i*2+1].e) {
			t.nodes[i].e = append(t.nodes[i].e, t.nodes[i*2].e[p])
			p++
		} else if p == len(t.nodes[i*2].e) {
			t.nodes[i].e = append(t.nodes[i].e, t.nodes[i*2+1].e[q])
			q++
		} else if t.nodes[i*2].e[p] < t.nodes[i*2+1].e[q] {
			t.nodes[i].e = append(t.nodes[i].e, t.nodes[i*2].e[p])
			p++
		} else {
			t.nodes[i].e = append(t.nodes[i].e, t.nodes[i*2+1].e[q])
			q++
		}
	}
}

func (t *mergeSortTree) init(e []int) {
	t.n = len(e)
	t.nodes = make([]treeNode, t.n*4)
	t.merge(1, 0, t.n-1, e)
}

func (t *mergeSortTree) find(i, l, r, ql, qr, k int) int {
	if r < ql || qr < l {
		return 0
	}
	if ql <= l && r <= qr {
		return len(t.nodes[i].e) - sort.SearchInts(t.nodes[i].e, k+1)
	}
	m := (l + r) / 2
	return t.find(i*2, l, m, ql, qr, k) + t.find(i*2+1, m+1, r, ql, qr, k)
}

// Get the number of elements larger than k in e[i...j].
func (t *mergeSortTree) query(i, j, k int) int {
	return t.find(1, 0, t.n-1, i, j, k)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)

	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &a[i])
	}

	t := new(mergeSortTree)
	t.init(a)

	var m int
	fmt.Fscan(in, &m)

	for l := 0; l < m; l++ {
		var i, j, k int
		fmt.Fscan(in, &i, &j, &k)
		fmt.Fprintln(out, t.query(i-1, j-1, k))
	}
}
