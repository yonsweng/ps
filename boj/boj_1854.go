package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
)

type Edge struct {
	node, cost int
}

type Item struct {
	cost, node int
}

type PriorityQueue []Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].cost < pq[j].cost
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(Item))
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[0 : n-1]
	return item
}

func getInput() (int, int, int, [][]Edge) {
	reader := bufio.NewReader(os.Stdin)
	var n, m, k int
	fmt.Fscan(reader, &n, &m, &k)

	edges := make([][]Edge, n+1)
	for i := 0; i < m; i++ {
		var a, b, c int
		fmt.Fscan(reader, &a, &b, &c)
		edges[a] = append(edges[a], Edge{b, c})
	}

	return n, m, k, edges
}

func solution(n, m, k int, edges [][]Edge) []int {
	adj := edges
	pq := &PriorityQueue{}
	heap.Init(pq)
	dist := make([][]int, n+1)
	heap.Push(pq, Item{0, 1})

	for pq.Len() > 0 {
		item := heap.Pop(pq).(Item)
		cost, node := item.cost, item.node

		if len(dist[node]) >= k {
			continue
		}
		dist[node] = append(dist[node], cost)

		for _, edge := range adj[node] {
			heap.Push(pq, Item{cost + edge.cost, edge.node})
		}
	}

	answer := make([]int, n+1)
	for i := 1; i <= n; i++ {
		if len(dist[i]) < k {
			answer[i] = -1
		} else {
			answer[i] = dist[i][k-1]
		}
	}

	return answer
}

func printAnswer(answer []int) {
	for i := 1; i < len(answer); i++ {
		fmt.Println(answer[i])
	}
}

func main() {
	n, m, k, edges := getInput()
	answer := solution(n, m, k, edges)
	printAnswer(answer)
}
