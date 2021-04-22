class Solution {
    public String getPermutation(int n, int k) {
        StringBuilder sb = new StringBuilder();
        ArrayList<Integer> num = new ArrayList<Integer>();
        int fact = 1;
        // calc factorials
        for (int i = 1; i <= n; i++) {
            fact *= i;
            num.add(i);
        }
        // zero-index k
        for (int i = 0, l = k - 1; i < n; i++) {
            // calc prev factorial
            fact /= (n - i);
            // get index of next item
            int index = (l / fact);
            // add item
            sb.append(num.remove(index));
            // update number
            l -= index * fact;
        }
        // convert to string
        return sb.toString();
    }
}