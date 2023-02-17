package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	var p []int
	fmt.Fscan(in, &n)
	for i := 0; i < n; i++ {
		var tmp int
		fmt.Fscan(in, &tmp)
		p = append(p, tmp)
	}

	sort.IntSlice(p).Sort()

	// accumulate p
	for i := 1; i < n; i++ {
		p[i] += p[i-1]
	}

	// sum p
	var sum int
	for i := 0; i < n; i++ {
		sum += p[i]
	}

	fmt.Println(sum)
}
