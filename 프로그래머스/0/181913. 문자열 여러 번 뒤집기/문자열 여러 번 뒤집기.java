import java.util.*;
// 문자열 여러 번 뒤집기
class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = my_string; // answer에 미리 my_string을 담아 놓고,

        for(int i = 0; i < queries.length; i++) { // queries 배열을 순회하면서
            String reverseTemp = answer.substring(queries[i][0], queries[i][1]+1); // 해당 길이의 배열을 담아놓고,
            String reverse = ""; // 거꾸로 만든 후 담아 놓을 문자열 변수
            String strTemp = ""; // 매번 계산해서 answer에 넣어줄 문자열 변수

            for(int j = reverseTemp.length() - 1; j >= 0; j--) { // 거꾸로 순회하면서 reverse문자열을 만들고,
                reverse += "" + reverseTemp.charAt(j);
            }

            strTemp += answer.substring(0, queries[i][0]); // 해당 부분 이전 문자열,
            strTemp += reverse; // 해당 부분 문자열,
            strTemp += answer.substring(queries[i][1]+1); // 이후 문자열을 담고
            answer = strTemp; //  answer에 넣어준다.
        }
        
        return answer;
    }
}