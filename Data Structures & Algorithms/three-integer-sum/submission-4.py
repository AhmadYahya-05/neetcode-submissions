class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        answer = set()

        for i in range(len(nums)):

            lp, rp = i + 1, len(nums) - 1
            
            target = -nums[i]

            while lp < rp:
                
                if nums[lp] + nums[rp] < target:
                    lp += 1
                elif nums[lp] + nums[rp] > target:
                    rp -= 1
                else:
                    answer.add((nums[i],nums[lp],nums[rp]))
                    lp += 1
                    rp -= 1

        array_of_arrays = [list(tup) for tup in answer]
        return array_of_arrays
        




        