class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        nums = [(p,s) for p,s in zip(position, speed)]
        nums.sort(reverse=True)

        for i in range(len(nums)):
            p,s = nums[i]
            t = (target-p) / s
            if stack and stack[-1] >= t:
                continue
                
            stack.append(t)

        return len(stack)