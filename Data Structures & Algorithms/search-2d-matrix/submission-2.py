class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #pretend this is 1-d and do binary search 
        # m is number or rows and n in number of cols
        m = len(matrix)
        n = len(matrix[0])

        l = 0 
        r = m*n -1 
        while l<=r:
            mid =(l+r)// 2
            rows = mid // n 
            cols = mid % n 
            val = matrix[rows][cols]

            if val == target:
                return True 
            elif val < target:
                l = mid+1

            else:
                r = mid - 1
        return False

        


            

        