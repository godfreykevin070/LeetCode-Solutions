class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = ""
        length = 0

        for i in s:
            if i not in string:
                string += i
                length = max(length, len(string))
            else:
                index = string.index(i)+1
                string = string[index:]
                string += i

        return length
    