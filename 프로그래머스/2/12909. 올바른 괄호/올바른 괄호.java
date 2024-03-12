import java.util.Stack;
// 올바른 괄호
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        // String[] sArr = s.split("");
        // Stack<String> stack = new Stack<>();
        
        // for(int i = 0; i < sArr.length; i++) {
        //     if(stack.size() == 0) {
        //         if(sArr[i].equals(")")) {
        //             stack.push(sArr[i]);
        //             break;
        //         }
        //         stack.push(sArr[i]);
        //     } else {
        //         if (sArr[i].equals("(") && stack.peek().equals(")")) {
        //             break;
        //         } else {
        //             if(sArr[i].equals(")") && stack.peek().equals("(")) {
        //                 stack.pop();
        //             } else {
        //                 stack.push(sArr[i]);
        //             }
        //         }
        //     }
        // }
        
        // for (int i = 0; i < sArr.length; i++) {  
        //     if (sArr[i].equals ("(")) {  
        //         stack.push("(");  
        //     } else if (sArr[i].equals(")")) {  
        //         if (stack.isEmpty()) {  
        //             return false;  
        //         }  
        //         stack.pop();  
        //     }  
        // }  
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {  
            if (s.charAt(i) == '(') {  
                stack.push('(');  
            } else if (s.charAt(i) == ')') {  
                if (stack.isEmpty()) {  
                    return false;  
                }  
                stack.pop();  
            }  
        }
        
        if(stack.size() != 0) answer = false;

        return answer;
    }
}