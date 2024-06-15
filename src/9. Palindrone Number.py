# https://leetcode.com/problems/palindrome-number/description/ for question

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        y =x[::-1]
        if x == y:
            return True
        else:
            return False