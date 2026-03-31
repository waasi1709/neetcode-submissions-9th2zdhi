class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count_t = defaultdict(int)
        for char in t:
            count_t[char] += 1

        count_s = defaultdict(int)
        need = len(count_t)
        have = 0 
        l = 0
        reslen = float("infinity")
        res = [-1,-1]

        for r in range(len(s)):
            count_s[s[r]] += 1

            if s[r] in count_t and count_t[s[r]] == count_s[s[r]]:
                have += 1

            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = (r-l+1)

                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l+=1

        l,r = res
        return s[l:r+1] if reslen != float("infinity") else ""







        





        