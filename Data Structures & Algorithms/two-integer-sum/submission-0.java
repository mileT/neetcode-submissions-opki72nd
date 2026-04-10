class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> numIndexMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int second = target - nums[i];
            if (numIndexMap.containsKey(second)) {
                result[0] = numIndexMap.get(second);
                result[1] = i;
                return result;
            }
            numIndexMap.put(nums[i], i);
        }
        return result;
        
    }
}
