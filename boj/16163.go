package main

import (
	"bufio"
	"fmt"
	"os"
)

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func main() {
	var s = []rune{'#'}

	var ss string
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &ss)
	for _, c := range ss {
		s = append(s, c)
		s = append(s, '#')
	}
	// for i := 0; i < 1000000; i++ {
	// 	s = append(s, 'A')
	// 	s = append(s, '#')
	// 	s = append(s, 'B')
	// 	s = append(s, '#')
	// }

	d := make([]int, len(s))
	p := 0
	v := 0
	for i := 1; i < len(d); i++ {
		if i <= v {
			d[i] = min(d[2*p-i], v-i)
		}
		for i-d[i]-1 >= 0 && i+d[i]+1 < len(d) && s[i-d[i]-1] == s[i+d[i]+1] {
			d[i]++
		}
		if i+d[i] > v {
			p = i
			v = i + d[i]
		}
	}

	answer := 0
	for i, di := range d {
		if i%2 == 0 {
			answer += di / 2
		} else {
			answer += (di + 1) / 2
		}
	}

	fmt.Print(answer)
}
