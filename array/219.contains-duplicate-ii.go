/*
 * @lc app=leetcode id=219 lang=golang
 *
 * [219] Contains Duplicate II
 */
// package main

func containsNearbyDuplicate(nums []int, k int) bool {
	m := make(map[int]int)
	m2 := make(map[int]int)
	for idx, val := range nums {
		if i, ok := m[val]; ok {
			if diff, inner_ok := m2[val]; inner_ok {
				if idx-i < diff {
					m2[val] = idx - i
				}
			} else {
				m2[val] = idx - i
			}
		}

		m[val] = idx
	}
	for _, diff := range m2 {
		if diff <= k {
			return true
		}
	}

	return false
}

// func main() {
// 	// data := []int{1, 2, 3, 1}
// 	// data := []int{1, 0, 1, 1}
// 	data := []int{1, 2, 3, 1, 2, 3}
// 	res := containsNearbyDuplicate(data, 2)
// 	fmt.Println(res)
// }
// √ Accepted
//   √ 23/23 cases passed (16 ms)
//   √ Your runtime beats 80 % of golang submissions
//   √ Your memory usage beats 24.47 % of golang submissions (9 MB)