package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func countOnes(x uint32) int {
	// Count the number of 1s in the binary representation of x
	count := 0
	for x > 0 {
		count++
		x &= x - 1 // Remove the lowest set bit
	}
	return count
}

func countMinPegs(nonPlayable map[[2]int]bool, memo map[uint32]int, pegs uint32) int {
	// Check if we've already computed this state
	if result, exists := memo[pegs]; exists {
		return result
	}

	minPegs := countOnes(pegs)

	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			if nonPlayable[[2]int{i, j}] {
				continue
			}

			// Continue if it is not a peg
			if (pegs & (1 << uint(i*5+j))) == 0 {
				continue
			}

			// Check the four possible directions for a jump
			directions := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
			for _, dir := range directions {
				di, dj := dir[0], dir[1]
				ni, nj := i+di, j+dj
				if ni < 0 || ni >= 5 || nj < 0 || nj >= 5 || nonPlayable[[2]int{ni, nj}] {
					continue
				}

				// Continue if there is no peg to jump over
				if (pegs & (1 << uint(ni*5+nj))) == 0 {
					continue
				}

				visitedEmpty := false

				for k := 2; k < 3; k++ {
					ni2, nj2 := i+k*di, j+k*dj
					if ni2 < 0 || ni2 >= 5 || nj2 < 0 || nj2 >= 5 || nonPlayable[[2]int{ni2, nj2}] {
						break
					}

					// Continue if there is a peg at the landing position
					if pegs&(1<<uint(ni2*5+nj2)) != 0 {
						if visitedEmpty {
							break
						}
						continue
					}

					visitedEmpty = true

					// Create a new state after the jump
					newPegs := pegs
					for m := 1; m < k; m++ {
						ni3, nj3 := i+m*di, j+m*dj
						newPegs ^= 1 << uint(ni3*5+nj3) // Remove the peg being jumped over
					}
					newPegs ^= 1 << uint(i*5+j)     // Remove the peg at the starting position
					newPegs |= 1 << uint(ni2*5+nj2) // Add the peg at the landing position

					result := countMinPegs(nonPlayable, memo, newPegs)
					if result < minPegs {
						minPegs = result
					}
				}
			}
		}
	}

	memo[pegs] = minPegs
	return minPegs
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < n; i++ {
		var board [5]string
		for j := 0; j < 5; j++ {
			scanner.Scan()
			board[j] = scanner.Text()
		}

		nonPlayable := make(map[[2]int]bool)
		var pegs uint32 = 0
		for i := 0; i < 5; i++ {
			for j := 0; j < 5; j++ {
				if board[i][j] == '#' {
					nonPlayable[[2]int{i, j}] = true
				} else if board[i][j] == 'o' {
					pegs |= 1 << uint(i*5+j)
				}
			}
		}

		// Replace the fixed-size array with a map
		memo := make(map[uint32]int)

		fmt.Fprintf(writer, "The best case ends with %d pegs.\n", countMinPegs(nonPlayable, memo, pegs))
	}
}
