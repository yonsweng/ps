package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m int
	fmt.Fscan(in, &n)
	d := make(map[int]bool, n)
	for i := 0; i < n; i++ {
		var k int
		fmt.Fscan(in, &k)
		d[k] = true
	}
	fmt.Fscan(in, &m)
	for i := 0; i < m; i++ {
		var k int
		fmt.Fscan(in, &k)
		if d[k] {
			fmt.Fprint(out, 1, " ")
		} else {
			fmt.Fprint(out, 0, " ")
		}
	}
}
