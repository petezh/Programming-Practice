class Solution {
    public boolean exist(char[][] board, String word) {
        char[] w = word.toCharArray();
        // explore from every square
        for (int y=0; y<board.length; y++) {
            for (int x=0; x<board[y].length; x++) {
                if (exist(board, y, x, w, 0)) return true;
            }
        }
        return false;
    }

    private boolean exist(char[][] board, int y, int x, char[] word, int i) {
        // found word
        if (i == word.length) return true;
        // out of bound
        if (y<0 || x<0 || y == board.length || x == board[y].length) return false;
        // letter doesnt match
        if (board[y][x] != word[i]) return false;
        // mark as occupied
        board[y][x] ^= 256;
        // recurse
        boolean exist = exist(board, y, x+1, word, i+1)
            || exist(board, y, x-1, word, i+1)
            || exist(board, y+1, x, word, i+1)
            || exist(board, y-1, x, word, i+1);
        board[y][x] ^= 256;
        return exist;
    }
}