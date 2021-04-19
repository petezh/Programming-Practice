public class Solution {

	public int jump(int[] A) {
        // initialize
        int jumps = 0, start = 0, end = 0;
        // iterate
        for(int i = 0; i < A.length-1; i++) {
            // update farthest end
            end = Math.max(end, i+A[i]);
            // update start
            if(i == start){
                start = end;
                jumps++;
                if(end > A.length){
                    break;
                }
            }
        }
        return jumps;
        
	}
}