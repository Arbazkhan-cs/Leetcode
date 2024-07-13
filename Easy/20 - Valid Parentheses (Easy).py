class Solution:
    def isValid(self, s: str) -> bool:
        parenTheses = [")", "}", "]"]
        stack = []
        for c in s:
            if c not in parenTheses:
                stack.append(c)
            else:
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False
                stack.pop()

        return not stack 
