import "fmt"

/*
 * @lc app=leetcode id=229 lang=golang
 *
 * [229] Majority Element II
 *
 * https://leetcode.com/problems/majority-element-ii/description/
 *
 * algorithms
 * Medium (32.11%)
 * Likes:    845
 * Dislikes: 102
 * Total Accepted:    101.2K
 * Total Submissions: 315.1K
 * Testcase Example:  '[3,2,3]'
 *
 * Given an integer array of size n, find all elements that appear more than ⌊
 * n/3 ⌋ times.
 *
 * Note: The algorithm should run in linear time and in O(1) space.
 *
 * Example 1:
 *
 *
 * Input: [3,2,3]
 * Output: [3]
 *
 * Example 2:
 *
 *
 * Input: [1,1,1,3,3,2,2,2]
 * Output: [1,2]
 *
 */

// package main

// import "fmt"

func majorityElement(nums []int) []int {

	res := make([]int, 0)
	if len(nums) == 0 {
		return res
	}
	temp := make(map[int]int)
	length := len(nums) / 3
	fmt.Println(length)
	for _, val := range nums {
		if _, ok := temp[val]; ok {
			temp[val]++
		} else {
			temp[val] = 1
		}
	}

	for k, v := range temp {
		if v > length {
			res = append(res, k)
		}
	}

	return res

}

// func main() {
// 	data := []int{1, 1, 1, 3, 3, 2, 2, 2}
// 	res := majorityElement(data)
// 	fmt.Println(res)
// }

// √ Accepted
//   √ 66/66 cases passed (12 ms)
//   √ Your runtime beats 82.27 % of golang submissions
//   √ Your memory usage beats 28.42 % of golang submissions (5.1 MB)
