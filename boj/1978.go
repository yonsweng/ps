package main

import (
	"fmt"
	"math"
)

func sieveOfEratosthenes(isPrime []bool) {
	for i := range isPrime {
		isPrime[i] = true
	}
	isPrime[1] = false
	for i := 2; i <= int(math.Sqrt(1000)); i++ {
		if !isPrime[i] {
			continue
		}
		for j := i * 2; j <= 1000; j += i {
			isPrime[j] = false
		}
	}
}

func main() {
	var N int
	fmt.Scanln(&N)
	var a []int
	for i := 0; i < N; i++ {
		var ai int
		fmt.Scan(&ai)
		a = append(a, ai)
	}

	isPrime := make([]bool, 1001)
	sieveOfEratosthenes(isPrime)

	cnt := 0
	for i := 0; i < N; i++ {
		if isPrime[a[i]] {
			cnt += 1
		}
	}

	fmt.Print(cnt)
}
