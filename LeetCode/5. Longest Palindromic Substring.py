class Solution:
    def getLongestPalindrome(self, s: str, left, right) -> tuple:
        if not s:
            return s
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 1, left + 1)

    def longestPalindrome(self, s: str) -> str:
        t = (0, 0) #(lengthOfSubstring, startIndex)
        for i in range(len(s)):
            t = max(t, Solution.getLongestPalindrome(self, s, i, i)) # odd
            t = max(t, Solution.getLongestPalindrome(self, s, i, i + 1)) # even
        
        return s[t[1] : t[0] + t[1]] 