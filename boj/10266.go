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

func getPi(p string) []int {
	m := len(p)
	pi := make([]int, m)
	for i, j := 1, 0; i < m; i++ {
		for j > 0 && p[i] != p[j] {
			j = pi[j-1]
		}
		if p[i] == p[j] {
			j++
			pi[i] = j
		}
	}
	return pi
}

func kmp(s, p string) []int {
	ans := make([]int, 0)
	n, m := len(s), len(p)
	pi := getPi(p)
	for i, j := 0, 0; i < n; i++ {
		for j > 0 && s[i] != p[j] {
			j = pi[j-1]
		}
		if s[i] == p[j] {
			j++
			if j == m {
				ans = append(ans, i-m+1)
				j = pi[j-1]
			}
		}
	}
	return ans
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	var a [720000]byte
	var b [360000]byte
	for i := 0; i < 360000; i++ {
		a[i] = '0'
		a[i+360000] = '0'
		b[i] = '0'
	}
	fmt.Fscan(in, &n)
	for i := 0; i < n; i++ {
		var c int
		fmt.Fscan(in, &c)
		a[c] = '1'
		a[c+360000] = '1'
	}
	for i := 0; i < n; i++ {
		var c int
		fmt.Fscan(in, &c)
		b[c] = '1'
	}

	s := string(a[:])
	p := string(b[:])
	ans := kmp(s, p)
	if len(ans) > 0 {
		fmt.Fprintln(out, "possible")
	} else {
		fmt.Fprintln(out, "impossible")
	}
}
