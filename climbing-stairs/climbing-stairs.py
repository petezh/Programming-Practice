class Solution(object):
    def __init__(self):
        # base cases
        self.dic = {1:1, 2:2}

    def climbStairs(self, n):
        # memoize
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]