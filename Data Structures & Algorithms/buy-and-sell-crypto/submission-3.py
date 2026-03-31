class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #res = []
        #if len(prices) <=1:
        #    res.append(0)
        #for i in range(len(prices)):
            #for j in range(i+1,len(prices)):
            #    if prices[j] >= prices[i]:
           #         res.append(prices[j] - prices[i])
          #      else:
         #           res.append(0)

                

        #return max(res)

        #attempt a O(n) solution 
        l,r = 0,1
        maxP = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l=r
            r+=1

        return maxP

            




        