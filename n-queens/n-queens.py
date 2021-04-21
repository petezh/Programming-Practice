class Solution(object):
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            # num queens
            p = len(queens)
            # if done
            if p==n:
                result.append(queens)
                return None
            # else, try every spot
            for q in range(n):
                # check no horizontal or diagonal conflict
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    # recurse
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        # initialize
        result = []
        DFS([],[],[])
        # format sol
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]