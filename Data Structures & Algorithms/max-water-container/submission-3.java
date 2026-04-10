class Solution {
    public int maxArea(int[] heights) {
        int result = 0;
        int n = heights.length;
        int left = 0, right = n - 1;

        while (left < right) {
            int lowwerHeight = Math.min(heights[left], heights[right]);
            result = Math.max(result, (right - left) * lowwerHeight);
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return result;
    }
}
