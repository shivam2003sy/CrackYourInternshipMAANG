class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
            if nums[j]==0:
                nums.pop(j)
                nums.append(0)
                j-=1
            else:
                j-=1
                
            
                
                
            
            
            
            
            
            
                
                
            