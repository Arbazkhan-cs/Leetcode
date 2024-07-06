class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        temp_x = x
        rev_x = 0
        while temp_x:
            rev_x = (rev_x * 10) + (temp_x % 10)
            temp_x = temp_x//10
        
        return x == rev_x