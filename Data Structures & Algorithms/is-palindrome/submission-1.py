import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pattern = r'[^a-zA-Z0-9]'
        # cleaned_s = re.sub(pattern, '',s).lower()
        # return cleaned_s == cleaned_s[::-1]
        s_lowered = s.lower()
        l = 0 
        r = len(s_lowered)-1
        while l < r : 
            while l < r and not s_lowered[l].isalnum():
                l +=1 
            while l < r and not s_lowered[r].isalnum():
                r-=1
            if s_lowered[l] == s_lowered[r]:
                l +=1 
                r -=1 
            else:
                return False 
        return True 



