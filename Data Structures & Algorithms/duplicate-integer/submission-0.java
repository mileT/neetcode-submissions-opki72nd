class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> dupSet = new HashSet<>();
        for (int num : nums) {
            if (dupSet.contains(num)) {
                return true;
            }
            dupSet.add(num);
        }
        return false;
    }
}
