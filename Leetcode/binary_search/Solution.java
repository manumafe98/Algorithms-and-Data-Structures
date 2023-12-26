package Leetcode.binary_search;

class Solution {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end) {
            // Alternative formula to calculate the midpoint ((end - start) / 2) + start;
            int mid = (end + start) / 2;

            if (nums[mid] == target) return mid;

            if (nums[mid] > target) end = mid - 1;
            else start = mid + 1;
        }

        return -1;
    }
}
