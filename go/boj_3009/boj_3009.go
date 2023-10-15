package main

import "fmt"

func main() {
	var x, y [3]int
	for i := 0; i < 3; i++ {
		fmt.Scan(&x[i], &y[i])
	}
	if x[0] == x[1] {
		fmt.Print(x[2], " ")
	} else if x[0] == x[2] {
		fmt.Print(x[1], " ")
	} else if x[1] == x[2] {
		fmt.Print(x[0], " ")
	}
	if y[0] == y[1] {
		fmt.Print(y[2])
	} else if y[0] == y[2] {
		fmt.Print(y[1])
	} else if y[1] == y[2] {
		fmt.Print(y[0])
	}
}
