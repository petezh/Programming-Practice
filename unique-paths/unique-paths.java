public class Solution {
    public int uniquePaths(int m, int n) {
        // general idea: solve by computing combinatorial
        // catch 1 case
        if(m == 1 || n == 1)
            return 1;
        m--;
        n--;
        // swap them
        if(m < n) {              
            m = m + n;
            n = m - n;
            m = m - n;
        }
        long res = 1;
        for(int i = m+1, j = 1; i <= m+n; i++, j++){
            res *= i;
            res /= j;
        }
            
        return (int)res;
    }
}