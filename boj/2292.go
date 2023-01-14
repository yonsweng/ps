package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	i := 1
	for cur := 1; cur < n; i++ {
		cur += i * 6
	}

	fmt.Print(i)
}
