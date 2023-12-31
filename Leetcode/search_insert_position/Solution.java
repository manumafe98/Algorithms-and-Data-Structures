package Leetcode.search_insert_position;

class Solution {
    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end) {
            int mid = ((end - start) / 2) + start;

            if (nums[mid] == target)
                return mid;

            if (nums[mid] > target)
                end = mid - 1;
            else
                start = mid + 1;

        }
        return start;
    }
}
