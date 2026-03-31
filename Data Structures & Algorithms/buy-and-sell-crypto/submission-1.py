class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        if len(prices) <=1:
            res.append(0)
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] >= prices[i]:
                    res.append(prices[j] - prices[i])
                else:
                    res.append(0)

                

        return max(res)



        