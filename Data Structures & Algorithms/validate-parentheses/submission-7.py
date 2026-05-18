class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:

            if c in pairs.values():
                stack.append(c)

            else:
                if not stack:
                    return False

                stk_pop = stack.pop()

                if stk_pop != pairs[c]:
                    return False

        return len(stack) == 0