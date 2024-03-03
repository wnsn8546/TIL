import java.util.Stack;
// 같은 숫자는 싫어
public class Solution {
    public int[] solution(int []arr) {
        // 연속된 숫자가 나타나면 하나만 남긴다.
        Stack<Integer> stack = new Stack<>();
        
        for(int i = 0; i < arr.length; i++) {
            if(stack.size() == 0 || !(stack.peek() == arr[i])) {
                stack.push(arr[i]);
            }
        }
        
        int[] answer = new int[stack.size()];

        for(int i = stack.size() - 1; i >= 0; i--) {
            answer[i] = stack.pop();
        }
        
        return answer;
    }
}