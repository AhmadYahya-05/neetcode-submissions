class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [0] * len(nums)
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        #prefix array population
        prefix[0] = 1
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]

        #postfix array population
        postfix[len(nums) - 1] = 1
        for i in range(len(nums)-2,-1,-1):
            postfix[i] = postfix[i+1]*nums[i+1]

        for i in range(len(nums)):
            output[i] = prefix[i]*postfix[i]

            
        return output