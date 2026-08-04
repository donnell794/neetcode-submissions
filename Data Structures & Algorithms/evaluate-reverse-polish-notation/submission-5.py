class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        op = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv,}

        stack = []
        for t in tokens:
            if t not in op:
                stack.append(int(t))
                continue
            a,b = [stack.pop() for _ in range(2)]
            res = op[t](b, a)
            stack.append(int(res))


        return stack[0]