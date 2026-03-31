class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char.lower()
                

        rev_s = new_s[::-1]

        return new_s == rev_s





        