package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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

func max(arr []int) int {
	var max int
	for _, v := range arr {
		if v > max {
			max = v
		}
	}
	return max
}

func printOrder(priorities []int, target int) int {
	var order int
	q := &Queue{}

	for i := range priorities {
		q.Enqueue(i)
	}

	for !q.IsEmpty() {
		if priorities[q.Front()] < max(priorities) {
			q.Enqueue(q.Dequeue())
		} else {
			order++
			front := q.Dequeue()
			if front == target {
				return order
			}
			priorities[front] = 0
		}
	}

	return order
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < n; i++ {
		scanner.Scan()
		input := strings.Split(scanner.Text(), " ")
		num, _ := strconv.Atoi(input[0])
		target, _ := strconv.Atoi(input[1])

		scanner.Scan()
		input = strings.Split(scanner.Text(), " ")
		priorities := make([]int, num)
		for i, v := range input {
			priorities[i], _ = strconv.Atoi(v)
		}

		fmt.Println(printOrder(priorities, target))
	}
}
