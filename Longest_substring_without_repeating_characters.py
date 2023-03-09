class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        after, result = 0, 0
        used = [False for i in range(128)]
        for first in range(len(s)):
            while(after < len(s) and not used[ord(s[after])]):
                used[ord(s[after])] = True
                after += 1
            result = max(result, after - first)
            used[ord(s[first])] = False
        return result