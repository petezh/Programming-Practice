public class Solution {
    public int totalNQueens(int n) {
        boolean[] col = new boolean[n];
        boolean[] tlbr = new boolean[2 * n + 1]; // top left -> bottom right
        boolean[] trbl = new boolean[2 * n + 1]; // top right -> bottom left
        return tryPut(0, n, col, tlbr, trbl);
    }
    private int tryPut(int row, int size, boolean[] col, boolean[] tlbr, boolean[] trbl) {
        int result = 0;
        for (int i = 0; i < size; i++)
            if (!col[i] && !tlbr[size - 1 - row + i] && !trbl[row + i]) {
                // System.out.println("when row = " + row + ", try col = " + i);
                if (row == size - 1) {
                    result++;
                } else {
                    col[i] = true;
                    tlbr[size - 1 - row + i] = true;
                    trbl[row + i] = true;
                    result += tryPut(row + 1, size, col, tlbr, trbl);
                    col[i] = false;
                    tlbr[size - 1 - row + i] = false;
                    trbl[row + i] = false;
                }
            }
        return result;
    }
}