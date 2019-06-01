/*
 * @lc app=leetcode id=217 lang=golang
 *
 * [217] Contains Duplicate
 */
// package main

func containsDuplicate(nums []int) bool {
	m := make(map[int]bool)
	for _, val := range nums {
		if _, ok := m[val]; ok {
			return true
		} else {
			m[val] = true
		}
	}

	return false
}

// √ Accepted
//   √ 18/18 cases passed (24 ms)
//   √ Your runtime beats 60.07 % of golang submissions
//   √ Your memory usage beats 37 % of golang submissions (9.2 MB)
