package Leetcode.contains_duplicates;

import java.util.Map;
import java.util.HashMap;


public class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i : nums) {
            if (map.containsKey(i)) {
                return true;
            } else {
                map.put(i, 1);
            }
        }
        return false;
    }
}
