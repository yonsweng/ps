package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	answer := 1
	for i := 2; i <= N; i++ {
		answer *= i
	}
	fmt.Print(answer)
}
