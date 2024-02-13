import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        String[] numString = Integer.toString(n).split("");
        
        for(String s : numString) {
            answer += Integer.parseInt(s);
        }  
        
        return answer;
    }
}