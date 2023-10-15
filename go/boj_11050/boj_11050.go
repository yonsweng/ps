package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	wr = bufio.NewWriter(os.Stdout)
)

func binomialCoefficient(n, k int) int {
	if k == 0 || k == n {
		return 1
	}
	return binomialCoefficient(n-1, k-1) + binomialCoefficient(n-1, k)
}

func main() {
	defer wr.Flush()
	var n, k int
	fmt.Scan(&n, &k)
	fmt.Fprintln(wr, binomialCoefficient(n, k))
}
