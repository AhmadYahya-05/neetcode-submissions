class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

            left = 1
            right = max(piles)
            result = right

            while left <= right:                # [1.......12.......25]

                k = (left + right) // 2
                hours = 0

                for pile in piles:
                    hours += math.ceil(pile/k)
                
                if hours > h:
                    left = k + 1
                else:
                    right = k - 1
                    result = k

            return result
                    

            
        