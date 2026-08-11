class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths are different; if so, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Sort both strings and compare the results
        return sorted(s) == sorted(t)

        