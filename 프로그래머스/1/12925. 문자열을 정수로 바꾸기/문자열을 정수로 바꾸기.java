import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        boolean minus = false;
        String[] sArr = s.split("");
        String temp = "";
        
        if(sArr[0].equals("-")) {
            minus = true;
            for(int i = 1; i < sArr.length;i++) {
                temp += sArr[i];
            }
            answer = Integer.parseInt(temp);
            return answer *= -1;
        } else {
            for(int i = 0; i < sArr.length;i++) {
                temp += sArr[i];
            }
            answer = Integer.parseInt(temp);
            return answer;
        }
    }
}