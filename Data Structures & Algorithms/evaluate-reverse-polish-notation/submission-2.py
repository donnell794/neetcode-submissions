class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        for t in tokens:
            if t in ops:
                first, second = stack.pop(), stack.pop()
                stack.append(int(ops[t](second, first)))
            else:
                stack.append(int(t))

        return stack[0]

            