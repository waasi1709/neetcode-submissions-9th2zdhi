class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        dicti = { ")":"(" , "}":"{" , "]":"["}
        for char in s:
            if char in dicti:
                if stack and stack[-1] == dicti[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack

            

    





        