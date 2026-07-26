class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            
            if i > 0 and num == nums[i-1]:
                continue

            lp = i + 1
            rp = len(nums) - 1

            while lp < rp:

                if num + nums[lp] + nums[rp] < 0:
                    lp += 1

                elif num + nums[lp] + nums[rp] > 0:
                    rp -= 1

                else:
                    
                    result.append([num,nums[lp],nums[rp]])
                    lp += 1
                    
                    while nums [lp] == nums[lp - 1] and lp < rp:
                        lp += 1
        return result


            


            
            

            


