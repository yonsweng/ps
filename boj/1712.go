package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b, c int
	fmt.Scan(&a, &b, &c)
	if c <= b {
		fmt.Print(-1)
	} else {
		answer := int(math.Floor(float64(a)/float64(c-b))) + 1
		fmt.Print(answer)
	}
}
