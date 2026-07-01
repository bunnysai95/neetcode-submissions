class Solution:
    from collections import Counter 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        i = 0 
        j = 0 
        count = {}
        for char in s:
            count[char] = count.get(char, 0)+1 

        for char in t: 
            if char not in count: 
                return False 
            count[char] -=1 
            if count[char] < 0: 
                return False

        for value in count.values():
            if value !=0 :
                return False

        return True

        # while i < len(s) and j < len(t):
        #     if s[i] in t:
        #         i+=1 
        #     return False 
        # return True

        # return sorted(s) == sorted(t)
        # return Counter(s) == Counter(t)

