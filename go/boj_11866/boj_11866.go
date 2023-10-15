package main

import (
	"fmt"
)

type Queue struct {
	items []int
}

func (q *Queue) Enqueue(item int) {
	q.items = append(q.items, item)
}

func (q *Queue) Dequeue() int {
	item := q.items[0]
	q.items = q.items[1:]
	return item
}

func (q *Queue) IsEmpty() bool {
	return len(q.items) == 0
}

func (q *Queue) Front() int {
	return q.items[0]
}

func main() {
	var n, k int
	fmt.Scan(&n, &k)

	q := &Queue{}
	for i := 1; i <= n; i++ {
		q.Enqueue(i)
	}

	var result []int
	for !q.IsEmpty() {
		for i := 1; i < k; i++ {
			q.Enqueue(q.Dequeue())
		}
		result = append(result, q.Dequeue())
	}

	fmt.Print("<")
	for i, v := range result {
		if i == len(result)-1 {
			fmt.Printf("%d>", v)
		} else {
			fmt.Printf("%d, ", v)
		}
	}
}
