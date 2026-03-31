class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i,num in enumerate(nums):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res
        