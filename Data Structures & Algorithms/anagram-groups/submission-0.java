class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> anagramMap = new HashMap<>();
        for (String s : strs) {
            String key = countFreq(s);
            if (anagramMap.get(key) == null) {
                anagramMap.put(key, new ArrayList<String>());
            } 
            anagramMap.get(key).add(s);
        }
        return new ArrayList(anagramMap.values());
     

    }
    private String countFreq(String s) {
        int[] freqMap = new int[26];
        for (char c : s.toCharArray()) {
            freqMap[c -'a']++;
        }
        StringBuilder sb = new StringBuilder("*");
        for (int i = 0; i < 26; i++) {
            // sb.append(Character.toString((char) i));
            // sb.append(freqMap[i]);
            if (freqMap[i] > 0) {
                sb.append(Character.toString((char) i));
                sb.append(freqMap[i]);
            }
        }
        return sb.toString();
    }
}
