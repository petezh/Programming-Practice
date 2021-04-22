class Solution {
public:
    int lengthOfLastWord(string s) { 
        int len = 0, tail = s.length() - 1;
        // trailing whitespaces
        while (tail >= 0 && s[tail] == ' ') tail--;
        // count len
        while (tail >= 0 && s[tail] != ' ') {
            len++;
            tail--;
        }
        return len;
    }
};