# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:
# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

# Note: You may assume the string contain only lowercase letters.

def firstUniqChar(self, s: str) -> int:
    myMap = {}
    for i in s:
        if i in myMap:
            myMap[i] += 1
        else:
            myMap[i] = 1
    for j in range(len(s)):
        if myMap[s[j]] == 1:
            return j
    return -1