import java.util.*;
// 배열 만들기4
class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stk = new Stack<>();
        int i = 0;
        
        while(i < arr.length) {
            if (stk.size() == 0) {
                stk.push(arr[i]);
                i++;
            } else if(stk.size() > 0 && stk.peek() < arr[i]){
                stk.push(arr[i]);
                i++;
            } else if(stk.size() > 0 && stk.peek() >= arr[i]) {
                stk.pop();
            }
        }
        
        int[] answer = new int[stk.size()];
        for(int j = 0; j < stk.size() ; j++) {
            answer[j] = (int) stk.get(j);
        }
        
        return answer;
    }
}