class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = defaultdict(int)

        for char in s1:
            count_s1[char] += 1

        count_s2 = defaultdict(int)
        l= 0 
        for r in range(len(s2)):
            count_s2[s2[r]] += 1
            if (r-l+1) > len(s1):
                count_s2[s2[l]] -= 1

                if count_s2[s2[l]] == 0:
                    del count_s2[s2[l]]

                l+=1

            if count_s1 == count_s2:
                return True

        return False

            








        