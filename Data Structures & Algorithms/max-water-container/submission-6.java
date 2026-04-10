class Solution {
    public int maxArea(int[] heights) {
        int i = 0, j = heights.length - 1;
        int water = (j - i) * Math.min(heights[i], heights[j]);
        while (i < j) {
            water = Math.max(water, 
                (j - i) * Math.min(heights[i], heights[j]));
                if (heights[i] < heights[j]) {
                    i++;
                } else {
                    j--;
                }
        }
        return water;
    }
}
