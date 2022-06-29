class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=0
        f=1
        ans = 0
        while (f<len(prices)):
            if (prices[f] > prices[s]):
                profit =  prices[f]-prices[s]
                ans  = max(ans,profit) 
            else:
                s=f
            f+=1
                
        return ans 
            
        