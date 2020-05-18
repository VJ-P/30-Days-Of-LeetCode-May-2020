# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.

# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
 
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = Counter(s1)
        len1 = len(s1)
        freq2 = Counter(s2[0:len1])
        string2 = list(s2)
        if freq1 == freq2:
            return True
        for i in range(len(s2)-len1):
            freq2[s2[i+len1]] = (freq2[s2[i+len1]] or 0) + 1
            if freq2[s2[i]] > 1:
                freq2[s2[i]] -= 1
            else:
                del freq2[s2[i]]
            if freq1 == freq2:
                return True
        return False