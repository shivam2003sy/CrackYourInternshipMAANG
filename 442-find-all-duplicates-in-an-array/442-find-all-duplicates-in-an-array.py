class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d ={}
        res =[]
        for i in nums :
            if i in d:
                res.append(i)
            else:
                d[i] = 1
        return res
                
        