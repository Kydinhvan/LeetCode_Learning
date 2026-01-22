# Last updated: 1/22/2026, 12:13:02 PM
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # given string, check if front and back are the same
        # out: true false
        # method: remove empty space and comma, for each letter, find it's mirror and check
        for char in s:
            if char.isalpha() == False and char.isnumeric() == False:
                s = s.replace(char,"")
            
        for i in range(len(s)//2):
            s1 = s[i].lower()
            s2 = s[len(s)-1-i].lower()
            if s1 != s2:
                return False

        return True



        
        