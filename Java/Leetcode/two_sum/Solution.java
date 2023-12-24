package Java.Leetcode.two_sum;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

    // O(n^2) solution, because indexOf loops over the array and that costs O(n) inside a loop that is already O(n)
    public int[] twoSum(int[] nums, int target) {

        Integer[] integerArray = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        List<Integer> list = Arrays.asList(integerArray);

        for (int i = 0; i < list.size(); i++) {
            int x = target - list.get(i);
            
            if (list.indexOf(x) != -1 && list.indexOf(x) != i) {
                return new int[] {i, list.indexOf(x)};
            }
        }
        return new int[] {0, 0};
    }
    
    // O(n) solution, using a hashmap instead the cost of looking is O(1)
    public int[] twoSum1(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer,Integer> map = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(target - nums[i])){
                result[1] = i;
                result[0] = map.get(target - nums[i]);
                break;
            }
            map.put(nums[i], i);
        }
        
        return result;
    }    
}
