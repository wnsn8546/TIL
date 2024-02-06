import java.util.*;

class Solution {
    public int solution(int order) {
        int answer = 0;
        // 
        String[] s = Integer.toString(order).split("");
        
        for(String c : s) {
            if (Integer.parseInt(c) == 3 || Integer.parseInt(c) == 6 || Integer.parseInt(c) == 9) {
                answer += 1;
            } 
        }
        
        
        
        
        
        
        return answer;
    }
}