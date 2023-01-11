package main

import "fmt"

func main() {
	var x, y int
	fmt.Scanln(&x)
	fmt.Scanln(&y)

	var answer int
	if x > 0 && y > 0 {
		answer = 1
	} else if x < 0 && y > 0 {
		answer = 2
	} else if x < 0 && y < 0 {
		answer = 3
	} else {
		answer = 4
	}
	fmt.Println(answer)
}
