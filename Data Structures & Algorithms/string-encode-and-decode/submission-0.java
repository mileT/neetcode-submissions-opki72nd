class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            sb.append((char)str.length()).append(str);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int i = 0, n = str.length();
        while (i < n) {
            int size = (int) str.charAt(i++);
            result.add(str.substring(i, i + size));
            i += size;
        }
        return result;
    }
}
