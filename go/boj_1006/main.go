package main

import (
	"bufio"
	"fmt"
	"os"
)

const INF int = 987654321

func bundle(cnt, w int) int {
	if cnt <= w {
		return 1
	}
	return 2
}

func min(nums ...int) int {
	min := nums[0]
	for _, num := range nums[1:] {
		if num < min {
			min = num
		}
	}
	return min
}

func solve(enemies []int, n, w int) int {
	// 0: 위 아래 모두 고려
	// 1: 아래만 고려
	// 2: 위만 고려
	if n == 1 {
		if enemies[1]+enemies[2] <= w {
			return 1
		}
		return 2
	}

	answer := INF
	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, 3)
	}
	for j := 0; j < 4; j++ {
		enemies_1 := enemies[1]
		enemies_n := enemies[n]
		enemies_1n := enemies[1+n]
		enemies_2n := enemies[2*n]

		if j == 0 {
			dp[1][0] = bundle(enemies[1]+enemies[1+n], w)
			dp[1][1] = 1
			dp[1][2] = 1
		} else if j == 1 {
			if enemies[1]+enemies[n] <= w {
				dp[1][0] = 2
				dp[1][1] = 1
				dp[1][2] = INF
				enemies[1] = INF
				enemies[n] = INF
			} else {
				continue
			}
		} else if j == 2 {
			if enemies[1+n]+enemies[2*n] <= w {
				dp[1][0] = 2
				dp[1][1] = INF
				dp[1][2] = 1
				enemies[1+n] = INF
				enemies[2*n] = INF
			} else {
				continue
			}
		} else if j == 3 {
			if enemies[1]+enemies[n] <= w && enemies[1+n]+enemies[2*n] <= w {
				dp[1][0] = 2
				dp[1][1] = INF
				dp[1][2] = INF
				enemies[1] = INF
				enemies[n] = INF
				enemies[1+n] = INF
				enemies[2*n] = INF
			} else {
				continue
			}
		}

		for i := 2; i <= n; i++ {
			dp[i][0] = min(
				dp[i-1][0]+bundle(enemies[i]+enemies[i+n], w),
				dp[i-1][1]+bundle(enemies[i+n]+enemies[i+n-1], w)+1,
				dp[i-1][2]+bundle(enemies[i]+enemies[i-1], w)+1,
				dp[i-2][0]+bundle(enemies[i]+enemies[i-1], w)+bundle(enemies[i+n]+enemies[i+n-1], w),
			)
			dp[i][1] = min(
				dp[i-1][0]+1,
				dp[i-1][2]+bundle(enemies[i]+enemies[i-1], w),
			)
			dp[i][2] = min(
				dp[i-1][0]+1,
				dp[i-1][1]+bundle(enemies[i+n]+enemies[i+n-1], w),
			)
		}

		if j == 0 {
			answer = min(answer, dp[n][0])
		} else if j == 1 {
			answer = min(answer, dp[n][2])
		} else if j == 2 {
			answer = min(answer, dp[n][1])
		} else if j == 3 {
			answer = min(answer, dp[n-1][0])
		}

		enemies[1] = enemies_1
		enemies[n] = enemies_n
		enemies[1+n] = enemies_1n
		enemies[2*n] = enemies_2n
	}
	return answer
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var t int
	fmt.Fscanln(reader, &t)
	for i := 0; i < t; i++ {
		var n, w int
		fmt.Fscanln(reader, &n, &w)
		enemies := make([]int, n*2+1)
		for j := 1; j <= n; j++ {
			fmt.Fscanf(reader, "%d ", &enemies[j])
		}
		for j := n + 1; j <= n*2; j++ {
			fmt.Fscanf(reader, "%d ", &enemies[j])
		}
		fmt.Fprintln(writer, solve(enemies, n, w))
	}
}
