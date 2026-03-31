class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in res:
                return [res[comp],i]
            res[num] = i
        