import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l<r:
            hours = 0
            k = (l+r) //2

            for p in piles:
                hours += math.ceil(p/k)

            if hours<=h:
                r = k 
            else:
                l =k +1

        return l             


            

            



            
                 



        