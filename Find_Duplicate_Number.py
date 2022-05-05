class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = []
        nums.sort()
        for i in range (len(nums)):
            if nums[i-1] == nums[i]:
                dup.append(nums[i-1])
        return dup[0]


'''
Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
'''
