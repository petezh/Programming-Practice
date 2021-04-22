class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        s, e = newInterval
        left, right = [], []
        for i in intervals:
            i_s, i_e = i
            if i_e < s:
                left.append(i)
            elif i_s > e:
                right.append(i)
            else:
                s = min(s, i_s)
                e = max(e, i_e)
        return left + [[s, e]] + right