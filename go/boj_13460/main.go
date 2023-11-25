package main

import "fmt"

var n, m int

func move(board [][]rune, red, blue, hole [2]int, dir int) ([2]int, [2]int, bool) {
	red_, blue_ := red, blue
	moved := false

	if dir == 0 { // up
		if red[1] == blue[1] {
			var first, second *[2]int
			if red[0] < blue[0] {
				first, second = &red_, &blue_
			} else {
				first, second = &blue_, &red_
			}
			for i := (*first)[0] - 1; i > 0; i-- {
				if board[i][(*first)[1]] == 'O' {
					(*first)[0] = i
					moved = true
					break
				} else if board[i][(*first)[1]] == '#' {
					break
				} else {
					(*first)[0] = i
					moved = true
				}
			}
			for i := (*second)[0] - 1; i > 0; i-- {
				if board[i][(*second)[1]] == 'O' {
					(*second)[0] = i
					moved = true
					break
				} else if board[i][(*second)[1]] == '#' || i == (*first)[0] {
					break
				} else {
					(*second)[0] = i
					moved = true
				}
			}
		} else {
			for _, color := range [2]*[2]int{&red_, &blue_} {
				for i := (*color)[0] - 1; i > 0; i-- {
					if board[i][(*color)[1]] == 'O' {
						(*color)[0] = i
						moved = true
						break
					} else if board[i][(*color)[1]] == '#' {
						break
					} else {
						(*color)[0] = i
						moved = true
					}
				}
			}
		}
	} else if dir == 1 { // right
		if red[0] == blue[0] {
			var first, second *[2]int
			if red[1] < blue[1] {
				first, second = &blue_, &red_
			} else {
				first, second = &red_, &blue_
			}
			for j := (*first)[1] + 1; j < m-1; j++ {
				if board[(*first)[0]][j] == 'O' {
					(*first)[1] = j
					moved = true
					break
				} else if board[(*first)[0]][j] == '#' {
					break
				} else {
					(*first)[1] = j
					moved = true
				}
			}
			for j := (*second)[1] + 1; j < m-1; j++ {
				if board[(*second)[0]][j] == 'O' {
					(*second)[1] = j
					moved = true
					break
				} else if board[(*second)[0]][j] == '#' || j == (*first)[1] {
					break
				} else {
					(*second)[1] = j
					moved = true
				}
			}
		} else {
			for _, color := range [2]*[2]int{&red_, &blue_} {
				for j := (*color)[1] + 1; j < m-1; j++ {
					if board[(*color)[0]][j] == 'O' {
						(*color)[1] = j
						moved = true
						break
					} else if board[(*color)[0]][j] == '#' {
						break
					} else {
						(*color)[1] = j
						moved = true
					}
				}
			}
		}
	} else if dir == 2 { // down
		if red[1] == blue[1] {
			var first, second *[2]int
			if red[0] < blue[0] {
				first, second = &blue_, &red_
			} else {
				first, second = &red_, &blue_
			}
			for i := (*first)[0] + 1; i < n-1; i++ {
				if board[i][(*first)[1]] == 'O' {
					(*first)[0] = i
					moved = true
					break
				} else if board[i][(*first)[1]] == '#' {
					break
				} else {
					(*first)[0] = i
					moved = true
				}
			}
			for i := (*second)[0] + 1; i < n-1; i++ {
				if board[i][(*second)[1]] == 'O' {
					(*second)[0] = i
					moved = true
					break
				} else if board[i][(*second)[1]] == '#' || i == (*first)[0] {
					break
				} else {
					(*second)[0] = i
					moved = true
				}
			}
		} else {
			for _, color := range [2]*[2]int{&red_, &blue_} {
				for i := (*color)[0] + 1; i < n-1; i++ {
					if board[i][(*color)[1]] == 'O' {
						(*color)[0] = i
						moved = true
						break
					} else if board[i][(*color)[1]] == '#' {
						break
					} else {
						(*color)[0] = i
						moved = true
					}
				}
			}
		}
	} else if dir == 3 { // left
		if red[0] == blue[0] {
			var first, second *[2]int
			if red[1] < blue[1] {
				first, second = &red_, &blue_
			} else {
				first, second = &blue_, &red_
			}
			for j := (*first)[1] - 1; j > 0; j-- {
				if board[(*first)[0]][j] == 'O' {
					(*first)[1] = j
					moved = true
					break
				} else if board[(*first)[0]][j] == '#' {
					break
				} else {
					(*first)[1] = j
					moved = true
				}
			}
			for j := (*second)[1] - 1; j > 0; j-- {
				if board[(*second)[0]][j] == 'O' {
					(*second)[1] = j
					moved = true
					break
				} else if board[(*second)[0]][j] == '#' || j == (*first)[1] {
					break
				} else {
					(*second)[1] = j
					moved = true
				}
			}
		} else {
			for _, color := range [2]*[2]int{&red_, &blue_} {
				for j := (*color)[1] - 1; j > 0; j-- {
					if board[(*color)[0]][j] == 'O' {
						(*color)[1] = j
						moved = true
						break
					} else if board[(*color)[0]][j] == '#' {
						break
					} else {
						(*color)[1] = j
						moved = true
					}
				}
			}
		}
	}

	return red_, blue_, moved
}

func bfs(board [][]rune, red, blue, hole [2]int) int {
	visited := make([][][]bool, n)
	for i := 0; i < n; i++ {
		visited[i] = make([][]bool, m)
		for j := 0; j < m; j++ {
			visited[i][j] = make([]bool, n*m)
		}
	}

	queue := make([][2][2]int, 0)
	move_cnts := make([]int, 0)
	queue = append(queue, [2][2]int{red, blue})
	move_cnts = append(move_cnts, 0)
	visited[red[0]][red[1]][blue[0]*m+blue[1]] = true

	for len(queue) > 0 {
		red, blue := queue[0][0], queue[0][1]
		move_cnt := move_cnts[0]
		queue = queue[1:]
		move_cnts = move_cnts[1:]

		for dir := 0; dir < 4; dir++ {
			red_, blue_, moved := move(board, red, blue, hole, dir)
			if moved {
				if blue_ == hole {
					continue
				} else if red_ == hole {
					return move_cnt + 1
				} else if move_cnt >= 9 {
					continue
				} else if !visited[red_[0]][red_[1]][blue_[0]*m+blue_[1]] {
					queue = append(queue, [2][2]int{red_, blue_})
					move_cnts = append(move_cnts, move_cnt+1)
					visited[red_[0]][red_[1]][blue_[0]*m+blue_[1]] = true
				}
			}
		}
	}

	return -1
}

func main() {
	fmt.Scan(&n, &m)

	board := make([][]rune, n)
	red, blue, hole := [2]int{}, [2]int{}, [2]int{}
	for i := 0; i < n; i++ {
		var s string
		fmt.Scan(&s)
		board[i] = []rune(s)
		for j := 0; j < m; j++ {
			if board[i][j] == 'R' {
				red = [2]int{i, j}
				board[i][j] = '.'
			} else if board[i][j] == 'B' {
				blue = [2]int{i, j}
				board[i][j] = '.'
			} else if board[i][j] == 'O' {
				hole = [2]int{i, j}
			}
		}
	}

	fmt.Println(bfs(board, red, blue, hole))
}
