import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^a-zA-Z0-9]'
        cleaned_s = re.sub(pattern, '',s).lower()
        return cleaned_s == cleaned_s[::-1]