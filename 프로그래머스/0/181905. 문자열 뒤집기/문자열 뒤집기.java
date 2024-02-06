import java.util.*;
 
class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = "";
        String[] split = my_string.split("");
        String mid = "";
        // mid 에 들어갈 문자열을 넣는다.
        for(int i = e; i >= s; i--) {
            mid += split[i];
        }
        // 앞부분에 들어갈 문자열을 answer에 더한다.
        for(int i = 0; i < s; i++) {
            answer += split[i];
        }
        // mid 문자열을 answer에 더한다.
        answer += mid;
        // 뒷부분에 들어갈 문자열을 answer에 더한다.
        for(int i = e+1; i < my_string.length();i++) {
            answer += split[i];
        }
        
        return answer;
    }
}