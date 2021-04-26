class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        // empty list
        result.add(new ArrayList<>());
        // for each number
        for(int n : nums){
            // for number of results so far
            int size = result.size();
            for(int i=0; i<size; i++){
                // pick a subset
                List<Integer> subset = new ArrayList<>(result.get(i));
                // append a number
                subset.add(n);
                // add new subset
                result.add(subset);
            }
        }
        return result;
    }
}