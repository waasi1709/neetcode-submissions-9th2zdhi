class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #O(n^2) solution
        #res = []
        #for i in range(len(heights)):
        #    for j in range(i+1, (len(heights))):
        #        res.append((min(heights[i],heights[j]) * (j-i)))

        #return max(res)

        #lets try a O(n) solution 
        res = []
        l = 0 
        r = len(heights) - 1
        while l<r:
            water = (r-l) * min(heights[l],heights[r])
            res.append(water)
            if heights[l] < heights[r]:
                l+=1
            else:
                r -=1

        return max(res)


            
            






        