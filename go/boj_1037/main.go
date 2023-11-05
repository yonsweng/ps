package main

import (
	"bufio"
	"fmt"
	"os"
)

func gcd(a, b int) int {
	if a < b {
		a, b = b, a
	}
	for b != 0 {
		r := a % b
		a, b = b, r
	}
	return a
}

func min(a ...int) int {
	m := a[0]
	for _, v := range a {
		if v < m {
			m = v
		}
	}
	return m
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	d := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &d[i])
	}

	// get lcm of d
	lcm := d[0]
	for i := 1; i < n; i++ {
		lcm = int(int64(lcm) * int64(d[i]) / int64(gcd(lcm, d[i])))
	}

	for i := 0; i < n; i++ {
		if d[i] == lcm {
			lcm *= min(d...)
			break
		}
	}

	fmt.Fprintln(out, lcm)
}
