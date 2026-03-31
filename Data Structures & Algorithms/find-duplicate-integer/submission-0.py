class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ognums = set()
        for num in nums:
            if num in ognums:
                return num 
            ognums.add(num)


        


        