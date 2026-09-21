class Solution:
    def trap(self, height: List[int]) -> int:
        x=0
        y=len(height)-1
        prev_height_x=height[0]
        prev_height_y=height[-1]
        curr_area=0
        total_area=0
        while x<y:
            if prev_height_x<=prev_height_y:
                x+=1
                if height[x]>prev_height_x:
                    prev_height_x=height[x]
                    total_area+=curr_area
                    curr_area=0
                else:
                    curr_area+=prev_height_x-height[x]
            else:
                y-=1
                if height[y]>prev_height_y:
                    prev_height_y=height[y]
                    total_area+=curr_area
                    curr_area=0
                else:
                    curr_area+=prev_height_y-height[y]
        total_area+=curr_area
        return total_area