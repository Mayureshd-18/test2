class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for i in tokens:
            try:
                stack.append(int(i))
            except:
                val1 = stack.pop()
                val2 = stack.pop()
                match i:
                    case "+":
                        stack.append(val1+val2)
                    case "-":
                        stack.append(val2-val1)
                    case "*":
                        stack.append(val1*val2)
                    case "/":
                        stack.append(int(val2/val1))

        return stack.pop()