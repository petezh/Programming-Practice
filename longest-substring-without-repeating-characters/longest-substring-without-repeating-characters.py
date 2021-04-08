class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        current = ""
        rest = s
        while rest:
            let, rest = rest[0], rest[1:]
            index = current.find(let)
            if index == -1:
                current += let
            else:
                maxlen = max(maxlen, len(current))
                current = current[index+1:] + let
        maxlen = max(maxlen, len(current))
        return maxlen
        