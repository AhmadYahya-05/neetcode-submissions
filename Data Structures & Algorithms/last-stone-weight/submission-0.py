class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        
        while len(stones) > 1:
            
            stones.sort()
            largest, large = stones[-1],stones[-2]

            if largest == large:
                stones.pop()
                stones.pop()

            if largest > large:
                stones[-1] = stones[-1] - stones[-2]
                stones.pop(-2)

        if len(stones) == 1: return stones[0]
        else: return 0

        

        
        