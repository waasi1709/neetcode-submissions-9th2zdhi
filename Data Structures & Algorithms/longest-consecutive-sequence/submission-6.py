class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seta = set(nums)
        max_length = []
        if not nums:
            return 0
        for s in seta:
            if (s-1) not in seta:
                length = 1
                while (s+1) in seta:
                    s+=1
                    length += 1
                max_length.append(length)
                    


        return max(max_length)
                




            





        