package main

import "fmt"

func sum(a int, b int) int {
	return a + b
}

func main() {
	fmt.Printf("Sum of 10 and 2 is %d.\n", sum(10, 2))
}
