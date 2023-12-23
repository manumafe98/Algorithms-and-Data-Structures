package Leetcode.valid_anagram;

import java.util.Map;
import java.util.HashMap;

public class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() > t.length() || t.length() > s.length()) return false;

        Map<Character, Integer> tMap = new HashMap<>();
        Map<Character, Integer> sMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char tchar = t.charAt(i);
            char schar = s.charAt(i);

            if (tMap.containsKey(tchar)) {
                tMap.put(tchar, tMap.get(tchar) + 1);
            } else {
                tMap.put(tchar, 1);
            }
            if (sMap.containsKey(schar)) {
                sMap.put(schar, sMap.get(schar) + 1);
            } else {
                sMap.put(schar, 1); 
            }
        }

        return tMap.equals(sMap);
    }
}
