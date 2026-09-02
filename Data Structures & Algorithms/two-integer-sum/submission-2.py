class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, n in enumerate(nums):
            complement = target - n

            if complement in seen:
                return [seen[complement], i]

            seen[n] = i
        
        
        
        
        
        # hashmap = {}

        # for index, value in enumerate(nums):
            
           # complement = target - value

          #  if complement in hashmap:
           #     return [hashmap[index], index]

          #  else:
            #    hashmap[index] = value

            


