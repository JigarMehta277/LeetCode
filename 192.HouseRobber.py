'''
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

'''

# We are recussively so we use DP

# Import stuff

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        @lru_cache(None)
        def dp(i):

            if i >= n:
                return 0

            val = nums[i]

            # res initialized to 0 becuase we are finding max
            # res can be initialzed to float('inf') if finding min
            res = 0

            res = max(res, val + dp(i + 2)) # rob this house
            res = max(res, dp(i + 1)) # skip this house

            return res

        return dp(0)