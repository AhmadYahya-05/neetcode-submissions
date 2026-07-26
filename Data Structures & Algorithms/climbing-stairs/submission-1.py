class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 3:
            return n

    # ways(n) = ways(n-1) + ways(n-2)

        prev_step = 3
        prev2_step = 2

        for i in range(4,n+1):
            curr = prev_step + prev2_step
            prev2_step = prev_step
            prev_step = curr

        return prev_step






        

        