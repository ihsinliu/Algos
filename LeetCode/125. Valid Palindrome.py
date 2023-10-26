class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not Solution.is_valid(self, s[left]): 
                left+=1
            while left < right and not Solution.is_valid(self, s[right]): 
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        
        return True
            


    def is_valid(self, c:chr) -> bool:
        return c.isalpha() or c.isdigit()

        