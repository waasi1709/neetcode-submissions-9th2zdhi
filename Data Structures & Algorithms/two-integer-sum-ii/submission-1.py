class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #try with two pointer approach
        for i,num in enumerate(numbers):
            for j,num in enumerate(numbers):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        





        