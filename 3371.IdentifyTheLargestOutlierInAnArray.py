'''
3371. Identify the Largest Outlier in an Array(Med)

You are given an integer array nums. This array contains n elements, where exactly n - 2 elements are special numbers. One of the remaining two elements is the sum of these special numbers, and the other is an outlier.

An outlier is defined as a number that is neither one of the original special numbers nor the element representing the sum of those numbers.

Note that special numbers, the sum element, and the outlier must have distinct indices, but may share the same value.

Return the largest potential outlier in nums.

 

Example 1:

Input: nums = [2,3,5,10]

Output: 10

Explanation:

The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.

Example 2:

Input: nums = [-2,-1,-3,-6,4]

Output: 4

Explanation:

The special numbers could be -2, -1, and -3, thus making their sum -6 and the outlier 4.
'''

# Include counter lib

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        counts = Counter(nums)
        outlier = float('-inf')

        for num in nums:
            counts[num] -= 1
            total_sum -= num

            if total_sum % 2 == 0 and counts[total_sum // 2] > 0:
                outlier = max(outlier, num)

            counts[num] += 1
            total_sum += num

        return outlier

