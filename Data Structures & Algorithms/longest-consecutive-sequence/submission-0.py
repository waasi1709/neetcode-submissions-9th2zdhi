class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Numset = set(nums)
        longest = 0
        for num in nums:
            if (num -1) not in Numset:
                length = 0 
                while (num + length ) in Numset:
                    length += 1
                longest = max(length,longest)
        return longest
   