class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i,currentList,currentSum):

            if currentSum == target:
                res.append(currentList.copy())
                return 

            if i >= len(nums) or currentSum > target:
                return
                
            currentList.append(nums[i])
            dfs(i,currentList,currentSum + nums[i])
            currentList.pop()
            dfs(i+1,currentList,currentSum)  
         
            return res

        return dfs(0,[],0)

        