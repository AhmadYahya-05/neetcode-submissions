class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        curr_max = 0
        lp, rp = 0, len(heights) - 1

        while lp < rp:
            
            curr_max = max(curr_max, 
            (rp - lp) * (min(heights[lp],heights[rp])))

            if heights[lp] > heights[rp]:
                rp -= 1

            else:
                lp += 1

        return curr_max






