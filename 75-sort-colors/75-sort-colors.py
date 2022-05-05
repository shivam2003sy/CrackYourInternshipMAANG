class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {0:0, 1:0, 2:0}
        for i in nums:
            d[i] = d[i]+1
        index = 0
        # print(hash_map)
        for i in range(d[0]):
            nums[index] = 0
            index += 1
        for i in range(d[1]):
            nums[index] = 1
            index+=1
        for i in range(d[2]):
            nums[index] = 2
            index+=1
            
        
            
        
        
                
            
                        