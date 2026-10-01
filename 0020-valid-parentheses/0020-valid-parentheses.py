class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['} 
        for char in s:
            if char in pairs.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[char]:
                    return False

        return not stack