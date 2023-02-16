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

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var m, n int
	fmt.Fscan(in, &m, &n)

	var isPrime [1000001]bool
	for i := 2; i <= 1000000; i++ {
		isPrime[i] = true
	}

	for d := 2; d <= 1000; d++ {
		if !isPrime[d] {
			continue
		}

		for i := d * 2; i <= 1000000; i += d {
			isPrime[i] = false
		}
	}

	for i := m; i <= n; i++ {
		if isPrime[i] {
			fmt.Fprintln(out, i)
		}
	}
}
