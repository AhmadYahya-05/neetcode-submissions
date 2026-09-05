class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0 
        lp,rp = 0,1

        while rp in range(len(prices)):
                
            if prices[lp] < prices[rp]:
                maxProfit = max(maxProfit, (prices[rp] - prices[lp]))
            
            else:
                lp = rp
            rp += 1

        
        return maxProfit 