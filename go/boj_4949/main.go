package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(s string) string {
	var stack []rune
	for _, c := range s {
		if c == '(' || c == '[' {
			stack = append(stack, c)
		} else if c == ')' {
			if len(stack) == 0 || stack[len(stack)-1] != '(' {
				return "no"
			}
			stack = stack[:len(stack)-1]
		} else if c == ']' {
			if len(stack) == 0 || stack[len(stack)-1] != '[' {
				return "no"
			}
			stack = stack[:len(stack)-1]
		}
	}
	if len(stack) == 0 {
		return "yes"
	}
	return "no"
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	for scanner.Scan() {
		line := scanner.Text()
		if line == "." {
			break
		}
		fmt.Fprintln(out, solve(line))
	}
}
