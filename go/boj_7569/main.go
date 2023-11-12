package main

import (
	"bufio"
	"fmt"
	"os"
)

// queue
type queue [][3]int

func (q *queue) push(v [3]int) {
	*q = append(*q, v)
}

func (q *queue) pop() [3]int {
	if q.isEmpty() {
		return [3]int{}
	}
	v := (*q)[0]
	*q = (*q)[1:]
	return v
}

func (q *queue) isEmpty() bool {
	return len(*q) == 0
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var M, N, H int
	fmt.Fscan(in, &M, &N, &H)

	var box [][][]int
	for i := 0; i < H; i++ {
		var floor [][]int
		for j := 0; j < N; j++ {
			var row []int
			for k := 0; k < M; k++ {
				var v int
				fmt.Fscan(in, &v)
				row = append(row, v)
			}
			floor = append(floor, row)
		}
		box = append(box, floor)
	}

	var q queue
	inQ := make(map[[3]int]bool)
	for i := 0; i < H; i++ {
		for j := 0; j < N; j++ {
			for k := 0; k < M; k++ {
				if box[i][j][k] == 1 {
					q.push([3]int{i, j, k})
					inQ[[3]int{i, j, k}] = true
				}
			}
		}
	}

	for len(q) > 0 {
		v := q.pop()
		inQ[v] = false
		i, j, k := v[0], v[1], v[2]
		for _, v := range [][3]int{{i - 1, j, k}, {i + 1, j, k}, {i, j - 1, k}, {i, j + 1, k}, {i, j, k - 1}, {i, j, k + 1}} {
			if 0 <= v[0] && v[0] < H && 0 <= v[1] && v[1] < N && 0 <= v[2] && v[2] < M && box[v[0]][v[1]][v[2]] == 0 && !inQ[v] {
				box[v[0]][v[1]][v[2]] = box[i][j][k] + 1
				q.push(v)
				inQ[v] = true
			}
		}
	}

	var max int
	for i := 0; i < H; i++ {
		for j := 0; j < N; j++ {
			for k := 0; k < M; k++ {
				if box[i][j][k] == 0 {
					fmt.Fprintln(out, -1)
					return
				}
				if box[i][j][k] > max {
					max = box[i][j][k]
				}
			}
		}
	}
	fmt.Fprintln(out, max-1)
}
