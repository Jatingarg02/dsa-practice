class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        i = 0
        longest = 0

        for j, ch in enumerate(s):
            if ch in seen and seen[ch] >= i:
                i = seen[ch] + 1

            seen[ch] = j
            longest = max(longest , j - i + 1)
        return longest