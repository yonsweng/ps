package main

import "fmt"

func isPrime(n int) bool {
	if n == 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func solve(n int) int {
	var cnt int
	for i := n + 1; i <= 2*n; i++ {
		if isPrime(i) {
			cnt++
		}
	}
	return cnt
}

func main() {
	for {
		var n int
		fmt.Scan(&n)
		if n == 0 {
			break
		}
		fmt.Println(solve(n))
	}
}
