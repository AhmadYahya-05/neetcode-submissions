class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        streak = 0
        longest = 0
        i = 0

        while i < len(nums):
            
            if nums[i] == 1:
                streak += 1

            else:
                streak = 0
            
            longest = max(longest,streak)
            i += 1

        return longest


             

            