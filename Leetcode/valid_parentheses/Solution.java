package Leetcode.valid_parentheses;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution {
    // O(n)
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char[] charArr = s.toCharArray();

        List<Character> openingBrackets = new ArrayList<>() {
            {
                add('{');
                add('[');
                add('(');
            }
        };

        List<Character> closingBrackets = new ArrayList<>() {
            {
                add('}');
                add(']');
                add(')');
            }
        };

        for (char ch : charArr) {
            if (openingBrackets.contains(ch)) {
                stack.push(ch);
            } else {
                if (stack.size() > 0 && openingBrackets.indexOf(stack.pop()) == closingBrackets.indexOf(ch)) {
                    continue;
                } else {
                    return false;
                }
            }
        }
        if (stack.size() == 0)
            return true;

        return false;
    }
}
