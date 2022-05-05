class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in dic:
                return [dic[diff],i]
            else:
                dic[n]=i
        
        """for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]"""
        