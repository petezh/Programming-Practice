class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # remove whitespace
        s = s.strip().lower()
        # witnessed flags
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            # sign must be at the front or after e
            if char in ['+', '-']:
                if i > 0 and s[i-1] != 'e':
                    return False
            # only one dot, no e
            elif char == '.':
                if met_dot or met_e: return False
                met_dot = True
            # only one e, before digits
            elif char == 'e':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            # find digits
            elif char.isdigit():
                met_digit = True
            else:
                return False
        # at least one digit
        return met_digit