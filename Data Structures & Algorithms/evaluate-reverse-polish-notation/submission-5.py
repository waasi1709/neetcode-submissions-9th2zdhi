class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in {"+","-","*","/"}:
                stack.append(int(tokens[i]))

            elif tokens[i] == "+":
                a = stack.pop()
                b = stack.pop()
                c = a+b 
                stack.append(c)

            elif tokens[i] == "-":
                a = stack.pop()
                b = stack.pop()
                c = b - a 
                stack.append(c)

            elif tokens[i] == "*":
                a = stack.pop()
                b = stack.pop()
                c = b*a
                stack.append(c)

            elif tokens[i] == "/":
                a = stack.pop()
                b = stack.pop()
                #ensure truncation and no floats allowed
                stack.append(int(b / a))

        return stack[-1]





        