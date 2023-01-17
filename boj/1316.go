package main

import (
	"bufio"
	"fmt"
	"os"
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

func is_group_word(word string) bool {
	var shown [26]bool
	for i := 0; i < len(word); i++ {
		if i != 0 && word[i-1] != word[i] && shown[int(word[i])-int('a')] {
			return false
		}
		shown[int(word[i])-int('a')] = true
	}
	return true
}

func main() {
	var n int
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n)
	answer := 0
	for i := 0; i < n; i++ {
		var word string
		fmt.Fscan(in, &word)
		if is_group_word(word) {
			answer++
		}
	}
	fmt.Print(answer)
}
