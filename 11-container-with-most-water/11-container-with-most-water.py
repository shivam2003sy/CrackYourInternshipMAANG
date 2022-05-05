class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l= 0
        r = len(height)-1
        while l<r:
            h=min(height[l], height[r])
            w = r-l
            if area < h*w:
                area = h*w
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return area
                
                        
        