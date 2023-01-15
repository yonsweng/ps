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
	var name string
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &name)
	fmt.Printf("Hello, %s!", name)
}
