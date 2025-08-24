package main

import (
    "bufio"
    "fmt"
    "math"
    "os"
    "strconv"
    "strings"
)

const INF = math.MaxInt64

type Point struct {
    x, y int
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func cost(i, j, x, y int, points []Point, dp [][]int) int {
    if dp[i][j] != INF {
        return dp[i][j]
    }

    if i == j {
        dp[i][j] = abs(points[i].x-x) + abs(points[i].y-y)
        return dp[i][j]
    }

    for k := i; k < j; k++ {
        dp[i][j] = min(
            dp[i][j],
            cost(i, k, x, points[k].y, points, dp)+
                cost(k+1, j, points[k+1].x, y, points, dp)+
                abs(points[k+1].x-x)+abs(points[k].y-y),
        )
    }

    return dp[i][j]
}

func solve() {
    scanner := bufio.NewScanner(os.Stdin)
    
    scanner.Scan()
    n, _ := strconv.Atoi(scanner.Text())
    
    points := make([]Point, n)
    for i := 0; i < n; i++ {
        scanner.Scan()
        line := strings.Fields(scanner.Text())
        x, _ := strconv.Atoi(line[0])
        y, _ := strconv.Atoi(line[1])
        points[i] = Point{x, y}
    }

    originX := points[0].x
    originY := points[n-1].y

    dp := make([][]int, n)
    for i := range dp {
        dp[i] = make([]int, n)
        for j := range dp[i] {
            dp[i][j] = INF
        }
    }

    answer := cost(0, n-1, originX, originY, points, dp)
    fmt.Println(answer)
}

func main() {
    solve()
}