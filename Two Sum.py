

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> seen = new HashMap<Integer, Integer>();
        int value;
        int remains;
        for(int i = 0; i<nums.length; i++)
        {
            value = nums[i];
            remains = target-value;
            if(seen.containsKey(remains))
            {
                return new int[] {i, seen.get(remains)};
            }
            else
            {
                seen.put(value, i);
            }
        }
        
        
        // for(int i = 0; i<nums.length; i++)
        // {
        //     for(int j = i+1; j<nums.length; j++)
        //     {
        //         if(nums[i] + nums[j] == target)
        //         {                    
        //            return new int[] {i,j};
        //         }
        //     }
        // }
        return new int[0];
}
}
