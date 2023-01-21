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

type dp struct {
	cnt [][]int
}

func (d *dp) init(r, c int) {
	d.cnt = make([][]int, r)
	for i := range d.cnt {
		d.cnt[i] = make([]int, c)
	}
	for i := range d.cnt {
		for j := range d.cnt[i] {
			d.cnt[i][j] = -1
		}
	}
}

func (d *dp) nCases(i, state, n, m int) int {
	if d.cnt[i][state] == -1 {
		if i == n*m {
			d.cnt[i][state] = 1
		} else {
			if (state & 1) == 1 {
				d.cnt[i][state] = d.nCases(i+1, state>>1, n, m)
			} else {
				vertical := 0
				if i/m < n-1 {
					vertical = d.nCases(i+1, (state>>1)|(1<<(m-1)), n, m)
				}
				horizontal := 0
				if i%m < m-1 && (state&2) == 0 {
					horizontal = d.nCases(i+2, state>>2, n, m)
				}
				d.cnt[i][state] = vertical + horizontal
			}
		}
	}
	return d.cnt[i][state] % 9901
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m int
	fmt.Fscan(in, &n, &m)

	d := new(dp)
	d.init(n*m+1, 1<<m)
	answer := d.nCases(0, 0, n, m)
	fmt.Fprintln(out, answer)
}
