class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def dfs(tmpList, candidates, target):
            for i,c in enumerate(candidates):
                d = target - c
                if d == 0:
                    result.append(tmpList + [c])
                    break
                elif d > 0:
                    dfs(tmpList + [c], candidates[i:], d)
                else: # d < 0
                    break
        dfs([], sorted(candidates), target)
        return result