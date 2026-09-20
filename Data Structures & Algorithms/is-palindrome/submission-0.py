class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return "".join(cleaned_s.split(" "))=="".join(cleaned_s[::-1].split(" "))
        