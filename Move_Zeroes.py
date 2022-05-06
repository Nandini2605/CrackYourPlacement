class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        for i in range (n):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        while count < n:
            nums[count] = 0
            count += 1
        print(nums)
        
        
'''
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]
'''
