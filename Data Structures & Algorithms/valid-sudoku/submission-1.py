class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check if each row contains any duplicate 
        
        for i in range(len(board)):
            seta = set()
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in seta:
                        return False
                    else: 
                        seta.add(board[i][j])

        #check if each col contains any duplicate 
        for j in range(len(board)):
            setb = set()
            for i in range(len(board[j])):
                if board[i][j] != ".":
                    if board[i][j] in setb:
                        return False
                    else: 
                        setb.add(board[i][j])
        

        #check if any sub box contains duplicates
        for box_row in [0,3,6]:
            for box_col in [0,3,6]:
                setc= set()
                for i in range(box_row , box_row+3):
                    for j in range(box_col, box_col+3):
                        if board[i][j] != ".":
                            if board[i][j] in setc:
                                return False
                            else: setc.add(board[i][j])
        
        return True
                        


        