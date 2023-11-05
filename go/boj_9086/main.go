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

	var t int
	fmt.Fscan(in, &t)
	for i := 0; i < t; i++ {
		var s string
		fmt.Fscan(in, &s)
		fmt.Fprintln(out, string(s[0])+string(s[len(s)-1]))
	}
}
