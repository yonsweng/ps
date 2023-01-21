package main

import (
	"bufio"
	"fmt"
	"os"
)

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func giveFlow(cap []map[int]int, src, sink int) int {
	prev := make([]int, len(cap))

	q := []int{src}
	visited := make([]bool, len(cap))
	visited[src] = true
	finished := false
	for len(q) > 0 && !finished {
		u := q[0]
		q = q[1:]
		for v := range cap[u] {
			if !visited[v] && cap[u][v] > 0 {
				prev[v] = u
				if v == sink {
					finished = true
					break
				}
				q = append(q, v)
				visited[v] = true
			}
		}
	}

	flow := 0
	for v := sink; prev[v] != 0; v = prev[v] {
		u := prev[v]
		flow = max(flow, cap[u][v])
	}
	for v := sink; prev[v] != 0; v = prev[v] {
		u := prev[v]
		cap[u][v] -= flow
		cap[v][u] += flow
	}

	return flow
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, p int
	fmt.Fscan(in, &n, &p)
	cap := make([]map[int]int, 2*n-1)
	for i := 0; i < p; i++ {
		var u, v int
		fmt.Fscan(in, &u, &v)
		uu, vv := u, v
		if u != 1 && u != 2 {
			uu += n - 2
		}
		if v != 1 && v != 2 {
			vv += n - 2
		}
		if cap[uu] == nil {
			cap[uu] = map[int]int{}
		}
		if cap[vv] == nil {
			cap[vv] = map[int]int{}
		}
		cap[uu][v] = 1
		cap[vv][u] = 1
	}
	for u := 3; u <= n; u++ {
		if cap[u] == nil {
			cap[u] = map[int]int{}
		}
		cap[u][u+n-2] = 1
	}

	totalFlow := 0
	for {
		flow := giveFlow(cap, 1, 2)
		if flow == 0 {
			break
		}
		totalFlow += flow
	}

	fmt.Fprintln(out, totalFlow)
}
