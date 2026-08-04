class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            prod = 0
            for digit in map(int, str(n)):
                prod += digit**2

            if prod in seen:
                return False

            seen.add(prod)
            n = prod

        return True