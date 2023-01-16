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
	var a, b, c int
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &a, &b, &c)

	m := a*60 + b + c
	h := m / 60 % 24
	m = m % 60
	fmt.Print(h, m)
}
