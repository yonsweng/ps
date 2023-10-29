package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	nLongs := n / 4
	for i := 0; i < nLongs; i++ {
		fmt.Print("long ")
	}
	fmt.Print("int")
}
