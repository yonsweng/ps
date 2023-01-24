// You can edit this code!
// Click here and start typing.
package main

import "fmt"

func main() {
	var a [21]int

	a[0] = 0
	a[1] = 1
	for i := 2; i <= 20; i++ {
		a[i] = a[i-2] + a[i-1]
	}

	var n int
	fmt.Scan(&n)
	fmt.Println(a[n])
}
