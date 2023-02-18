package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func getSuffixArray(s string) []int {
	n := len(s)
	t := 1
	g := make([]int, 2*n)
	tg := make([]int, n)
	sa := make([]int, n)

	for i := 0; i < n; i++ {
		sa[i] = i
		g[i] = int(s[i]) - int('a')
		g[n+i] = -1
	}

	for t <= n {
		cmp := func(i, j int) bool {
			if g[sa[i]] != g[sa[j]] {
				return g[sa[i]] < g[sa[j]]
			}
			return g[sa[i]+t] < g[sa[j]+t]
		}

		sort.Slice(sa, cmp)

		tg[sa[0]] = 0
		for i := 1; i < n; i++ {
			if cmp(i-1, i) {
				tg[sa[i]] = tg[sa[i-1]] + 1
			} else {
				tg[sa[i]] = tg[sa[i-1]]
			}
		}

		// copy tg to g
		for i := 0; i < n; i++ {
			g[i] = tg[i]
		}

		t <<= 1
	}
	return sa
}

func getLCP(s string, sa []int) []int {
	n := len(s)
	rank := make([]int, n)
	lcp := make([]int, n)

	for i := 0; i < n; i++ {
		rank[sa[i]] = i
	}

	h := 0
	for i := 0; i < n; i++ {
		if h > 0 {
			h--
		}
		if rank[i] == 0 {
			continue
		}
		j := sa[rank[i]-1]
		for j+h < n && i+h < n && s[j+h] == s[i+h] {
			h++
		}
		lcp[rank[i]] = h
	}
	return lcp
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var s string
	fmt.Fscan(in, &s)

	sa := getSuffixArray(s)
	lcp := getLCP(s, sa)

	// print sa and lcp seperated by space
	for i := 0; i < len(s); i++ {
		fmt.Fprintf(out, "%d ", sa[i]+1)
	}
	fmt.Fprintln(out, "")
	fmt.Fprint(out, "x ")
	for i := 1; i < len(s); i++ {
		fmt.Fprintf(out, "%d ", lcp[i])
	}
}
