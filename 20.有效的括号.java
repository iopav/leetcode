/*
 * @lc app=leetcode.cn id=20 lang=java
 *
 * [20] 有效的括号
 */

// @lc code=start

import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 == 1) {
            return false;
        }
        Stack<Character> stack = new Stack<Character>();
        for (Character c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            }
            else {
                if (stack.empty()) {
                    return false;
                }
                else if (isPair(stack.peek(), c)) {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
        }
        if (stack.empty()) {
            return true;
        }
        return false;
    }
    
    public boolean isPair(Character l, Character r) {
        if (l == '(' && r == ')') {
            return true;
        }
        if (l == '[' && r == ']') {
            return true;
        }
        if (l == '{' && r == '}') {
            return true;
        }
        return false;
    }

}
// @lc code=end

