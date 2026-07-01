class Solution:
    from collections import Counter 
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # i = 0 
        # j = 0 
        # while i < len(s) and j < len(t):
        #     if s[i] in t:
        #         i+=1 
        #     return False 
        # return True

        # return sorted(s) == sorted(t)
        return Counter(s) == Counter(t)

