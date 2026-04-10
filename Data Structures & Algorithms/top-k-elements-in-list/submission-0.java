class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if (k == nums.length) {
            return nums;
        }
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            int freq = freqMap.getOrDefault(num, 0);
            freqMap.put(num, freq + 1);
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>( 
            (n1, n2)  -> freqMap.get(n1) - freqMap.get(n2));
        
        for (int key : freqMap.keySet()) {
            pq.add(key);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        int[] result = new int[k];
        for (int i = k - 1; i >= 0; i--) {
            result[i] = pq.poll();
        }
        return result;
    }
}
