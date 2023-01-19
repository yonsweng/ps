package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
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
	var name string
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &name)

	n := len(name)
	var c int
	c = strings.Count(name, "c=")
	n -= c
	c = strings.Count(name, "c-")
	n -= c
	c = strings.Count(name, "dz=")
	n -= c
	c = strings.Count(name, "d-")
	n -= c
	c = strings.Count(name, "lj")
	n -= c
	c = strings.Count(name, "nj")
	n -= c
	c = strings.Count(name, "s=")
	n -= c
	c = strings.Count(name, "z=")
	n -= c

	fmt.Print(n)
}
