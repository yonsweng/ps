package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var k, n int
	var a []int
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	fmt.Sscanf(scanner.Text(), "%d %d", &k, &n)
	a = make([]int, k)
	for i := 0; i < k; i++ {
		scanner.Scan()
		fmt.Sscanf(scanner.Text(), "%d", &a[i])
	}

	l, r := 1, 1<<31-1
	for l <= r {
		mid := (l + r) / 2
		cnt := int64(0)
		for _, v := range a {
			cnt += int64(v / mid)
		}
		if cnt >= int64(n) {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	fmt.Println(r)
}
