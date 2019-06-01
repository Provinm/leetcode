/*
 * @lc app=leetcode id=228 lang=golang
 *
 * [228] Summary Ranges
 */
package main

import "fmt"

func summaryRanges(nums []int) []string {

	vec := make([]int, 0)
	res := make([]string, 0)

	for i := 0; i < len(nums); i++ {
		if len(vec) > 0 {
			if nums[i]-vec[len(vec)-1] > 1 {
				if len(vec) == 1 {
					res = append(res, fmt.Sprintf("%d", vec[0]))
				} else {
					res = append(res, fmt.Sprintf("%d->%d", vec[0], vec[len(vec)-1]))
				}
				vec = make([]int, 0)
			}
		}
		vec = append(vec, nums[i])
	}

	if len(vec) == 1 {
		res = append(res, fmt.Sprintf("%d", vec[0]))
	} else if len(vec) > 1 {
		res = append(res, fmt.Sprintf("%d->%d", vec[0], vec[len(vec)-1]))
	}

	return res
}

// func main() {
// 	data := []int{0, 1, 2, 4, 5, 7}
// 	res := summaryRanges(data)
// 	fmt.Println(res)
// }

// √ Accepted
//   √ 28/28 cases passed (0 ms)
//   √ Your runtime beats 100 % of golang submissions
//   √ Your memory usage beats 53.57 % of golang submissions (2 MB)
