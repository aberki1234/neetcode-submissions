class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        curr_area=0
        x=0
        y=len(heights)-1
        while x<y:
            curr_area=min(heights[x],heights[y])*(y-x)
            if curr_area>max_area:
                max_area=curr_area
            if heights[x]>heights[y]:
                y=y-1
            else:
                x=x+1
        return max_area