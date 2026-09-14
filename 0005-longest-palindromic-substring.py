class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        
        def check_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            palindrome_odd = check_center(i, i)
            if len(palindrome_odd) > len(longest):
                longest = palindrome_odd
                
            palindrome_even = check_center(i, i + 1)
            if len(palindrome_even) > len(longest):
                longest = palindrome_even
                
        return longest
