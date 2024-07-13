class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        left = 0
        maxLength = 0

        for right in range(len(s)):
            if s[right] in hashMap:
                left = max(left, hashMap[s[right]] + 1)
            
            hashMap[s[right]] = right
            maxLength = max(maxLength, right - left + 1)

        return maxLength
