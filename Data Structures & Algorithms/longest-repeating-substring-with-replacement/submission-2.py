class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #use hashmap to count occrences
        mapz = defaultdict(int)
        res = 0 

        l = 0 
        for r in range(len(s)):
            mapz[s[r]] += 1


            if (r-l+1) - max(mapz.values()) > k:
                mapz[s[l]] -= 1
                l+=1

            res = max(res, r-l+1)

        return res




        