package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	a := make([]int, 3)
	fmt.Fscan(in, &a[0], &a[1], &a[2])

	sort.Ints(a)

	// 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
	// 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
	// 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
	answer := 0
	if a[0] == a[1] && a[1] == a[2] {
		answer = 10000 + a[0]*1000
	} else if a[0] == a[1] {
		answer = 1000 + a[0]*100
	} else if a[1] == a[2] {
		answer = 1000 + a[1]*100
	} else {
		answer = a[2] * 100
	}

	fmt.Println(answer)
}
