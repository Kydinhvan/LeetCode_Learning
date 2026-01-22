// Last updated: 1/22/2026, 12:12:58 PM
/*      # constrain 1 flip (0->1)
        # type, sliding window
        # Expand right pointer to explore.
        # Shrink left pointer only when the window violates the constraint.
        # Track window size with right - left + 1 whenever the window is valid.*/
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int left = 0;
        int zero_count = 0; // constraint number of 0 < 2
        int max_length = 0;
        for (int right = 0;right<nums.length; right++){
            if (nums[right] == 0){
                zero_count += 1;
            };
            while (zero_count > 1){
                if (nums[left] == 0){
                    zero_count -= 1;
                };
                left +=1;

            };
            max_length = Math.max(max_length,right - left + 1);
        };
        return max_length;
    };
};