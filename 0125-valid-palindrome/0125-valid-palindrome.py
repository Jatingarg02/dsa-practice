class Solution(object):
    def isPalindrome(self, s):
        phrase = "".join(ch for ch in s.lower() if ch.isalnum())
        l, r = 0 , len(phrase) - 1
        while l < r:
            if phrase[l] != phrase[r]:
                return False
            l += 1
            r -= 1
        return True
            