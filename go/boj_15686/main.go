package main

import (
	"bufio"
	"fmt"
	"os"
)

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func minDist(i, m int, selected [][2]int, chicken [][2]int, house [][2]int) int {
	if m == 0 {
		sum := 0
		for _, h := range house {
			min := 100000
			for _, s := range selected {
				dist := abs(h[0]-s[0]) + abs(h[1]-s[1])
				if dist < min {
					min = dist
				}
			}
			sum += min
		}
		return sum
	}

	min := 100000
	for j := i; j < len(chicken); j++ {
		selected[m-1] = chicken[j]
		dist := minDist(j+1, m-1, selected, chicken, house)
		if dist < min {
			min = dist
		}
	}

	return min
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m int
	fmt.Fscan(in, &n, &m)

	var city [50][50]int
	var chicken [][2]int
	var house [][2]int
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Fscan(in, &city[i][j])
			if city[i][j] == 1 {
				house = append(house, [2]int{i, j})
			} else if city[i][j] == 2 {
				chicken = append(chicken, [2]int{i, j})
			}
		}
	}

	selected := make([][2]int, m)
	fmt.Fprintln(out, minDist(0, m, selected, chicken, house))
}
