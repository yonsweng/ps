package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const MOD = 1999

func main() {
	reader := bufio.NewReader(os.Stdin)
	readLine(reader)
	a := parseInts(readLine(reader))
	b := parseInts(readLine(reader))

	c := make([]int, 29)
	for _, bi := range b {
		p := 0
		for bi > 0 {
			c[p] += bi % 2
			bi /= 2
			p++
		}
	}

	ans1 := 0
	for _, ai := range a {
		pp := 1
		for i := 0; i < 29; i++ {
			ans1 = (ans1 + pp*(ai%2)*c[i]) % MOD
			ai /= 2
			pp = (pp * 2) % MOD
		}
	}

	aMin := make([][2]int, 30)
	aMax := make([][2]int, 30)
	bMin := make([][2]int, 30)
	bMax := make([][2]int, 30)
	for i := range aMin {
		aMin[i] = [2]int{-1, -1}
		aMax[i] = [2]int{-1, -1}
		bMin[i] = [2]int{-1, -1}
		bMax[i] = [2]int{-1, -1}
	}

	for k := 0; k <= 29; k++ {
		mask := (1 << (k + 1)) - 1
		for _, ai := range a {
			ai &= mask
			idx := (ai >> k) & 1
			if aMin[k][idx] == -1 || ai < aMin[k][idx] {
				aMin[k][idx] = ai
			}
			if aMax[k][idx] == -1 || ai > aMax[k][idx] {
				aMax[k][idx] = ai
			}
		}
		for _, bi := range b {
			bi &= mask
			idx := (bi >> k) & 1
			if bMin[k][idx] == -1 || bi < bMin[k][idx] {
				bMin[k][idx] = bi
			}
			if bMax[k][idx] == -1 || bi > bMax[k][idx] {
				bMax[k][idx] = bi
			}
		}
	}

	ans2 := 0
	for k := 0; k <= 29; k++ {
		mask := 1 << k
		if aMin[k][0] != -1 && bMin[k][0] != -1 {
			mask &= aMin[k][0] + bMin[k][0]
		}
		if aMin[k][1] != -1 && bMin[k][1] != -1 {
			mask &= aMin[k][1] + bMin[k][1]
		}
		if aMax[k][0] != -1 && bMax[k][1] != -1 {
			mask &= aMax[k][0] + bMax[k][1]
		}
		if aMax[k][1] != -1 && bMax[k][0] != -1 {
			mask &= aMax[k][1] + bMax[k][0]
		}
		ans2 |= mask
	}

	fmt.Println(ans1, ans2)
}

func readLine(reader *bufio.Reader) string {
	line, _ := reader.ReadString('\n')
	return strings.TrimSpace(line)
}

func parseInts(line string) []int {
	fields := strings.Fields(line)
	result := make([]int, len(fields))
	for i, field := range fields {
		result[i], _ = strconv.Atoi(field)
	}
	return result
}
