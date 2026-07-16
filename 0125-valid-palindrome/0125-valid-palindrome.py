import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=s.strip()
        s=re.sub(r'[^a-zA-Z0-9]', '', s)
        
        n=len(s)
        left,right=0,n-1

        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True