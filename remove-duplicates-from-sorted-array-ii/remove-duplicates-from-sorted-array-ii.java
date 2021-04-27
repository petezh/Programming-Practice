class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for (int n : nums)
            // re-index duplicates
            if (i < 2 || n > nums[i-2])
                nums[i++] = n;
        return i;
    }
}