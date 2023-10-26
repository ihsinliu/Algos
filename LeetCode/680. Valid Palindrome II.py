class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        t = Solution.find_diff(self, s, left, right)
        if t[0] >= t[1]:
            return True
        else:
            return Solution.is_palindrome(self, s, t[0]+1, t[1]) or Solution.is_palindrome(self, s, t[0], t[1]-1)
            


    def is_palindrome(self, s:str, left:int, right:int ) -> bool:
        t = Solution.find_diff(self, s, left, right)
        return t[0] >= t[1]

    def find_diff(self, s:str, left:int, right:int) -> tuple:
        while left < right and s[left] == s[right]:
            left+=1
            right-=1

        return (left, right)