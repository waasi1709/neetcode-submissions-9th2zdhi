class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #if empty string return empty string 
        if t == "":
            return ""

        #count character frequency in t 
        count_t = defaultdict(int)
        for char in t:
            count_t[char] += 1

        have = 0 
        need = len(count_t)
        l = 0 
        reslen = float("infinity")
        count_s = defaultdict(int)
        res = [-1,-1]
        for r in range(len(s)):
            count_s[s[r]] += 1

            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                have += 1

            while have == need:
                #check if current window length is less than reslen
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = r-l+1
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l+=1

        l,r = res

        return s[l:r+1] if reslen != float("infinity") else ""


            




    







        





        