package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getNums(str string, size int) []int {
	arr := make([]int, size) 
	var err error
	raw := strings.Split(strings.TrimSpace(str), " ")
	for i, num := range raw {
		arr[i], err = strconv.Atoi(num)	
		check(err)
	}
	return arr

}

func main() {
	f, err := os.Open("day5_sample.txt")
	check(err)
	defer f.Close()

	seeds := make([]int, 10)
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		text := scanner.Text()
		if strings.Contains(text, "seeds:") {
			seeds = getNums(strings.Split(text, ":")[1], 10)	
		}
	}
	fmt.Println(seeds)

}
