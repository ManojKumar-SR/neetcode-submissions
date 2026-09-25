class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                l = s[left + 1 : right+1]
                r = s[left: right]

                return (l == l[::-1] or r == r[::-1])

            left += 1
            right -= 1
        
        return True