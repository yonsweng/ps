package main

import (
	"bufio"
	"fmt"
	"math"
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

	var a, b, v int
	fmt.Fscan(in, &a, &b, &v)

	answer := int(math.Ceil((float64(v) - float64(b)) / (float64(a) - float64(b))))
	fmt.Fprintln(out, answer)
}
