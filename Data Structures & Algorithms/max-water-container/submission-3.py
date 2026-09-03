class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0

        lp, rp = 0, len(heights) - 1

        while lp < rp:

            cur_area = (rp-lp) * (min(heights[lp], heights[rp]))
            maxArea = max(cur_area, maxArea)

            if heights [lp] >= heights[rp]:
                rp -= 1 
            else:
                lp += 1

        return maxArea