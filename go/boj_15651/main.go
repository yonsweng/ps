package main

import (
	"bytes"
	"fmt"
	"strconv"
)

func main() {
	var n, m int
	fmt.Scan(&n, &m)

	var a []int
	for i := 1; i <= n; i++ {
		a = append(a, i)
	}

	var buf bytes.Buffer
	var f func(int)
	f = func(k int) {
		if k == m {
			for _, v := range a[:m] {
				buf.WriteString(strconv.Itoa(v))
				buf.WriteByte(' ')
			}
			buf.WriteByte('\n')
			return
		}
		for i := 1; i <= n; i++ {
			a[k] = i
			f(k + 1)
		}
	}
	f(0)
	fmt.Print(buf.String())
}
