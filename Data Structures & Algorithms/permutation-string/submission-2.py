class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = defaultdict(int)

        for char in s1:
            s1_count[char] += 1

        s2_count = defaultdict(int)
        l=0
        for r in range(len(s2)):
            s2_count[s2[r]] += 1
            if (r-l+1) > len(s1):
                s2_count[s2[l]] -= 1
                if s2_count[s2[l]] == 0:
                    del s2_count[s2[l]]
                l+=1

            if s1_count == s2_count:
                return True

        return False


            








        