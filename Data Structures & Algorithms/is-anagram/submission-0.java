class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int n = s.length();
        int[] sCounter = new int[26];
        int[] tCounter = new int[26];
        for (int i = 0; i < n; i++) {
            sCounter[s.charAt(i) - 'a']++;
            tCounter[t.charAt(i) - 'a']++;
        }
        for (int j = 0; j < 26; j++) {
            if (sCounter[j] != tCounter[j]) {
                return false;
            }
        }
        return true;
    }
}
