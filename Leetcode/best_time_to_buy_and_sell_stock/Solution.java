package Leetcode.best_time_to_buy_and_sell_stock;

public class Solution {
    public int maxProfit(int[] prices) {
        int min = Integer.MAX_VALUE;
        int diff = 0;

        for (int val : prices) {
            if (val < min) min = val;
            else {
                if (val - min > diff) diff = val - min;
            }
        }
        
        return diff;
    }
}
