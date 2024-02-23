import java.util.*;
// 배열의 유사도
class Solution {
    public int solution(String[] s1, String[] s2) {
        // s1를 리스트로 만들고, 리스트1에서 s2의 요소와 같은 문자열의 개수를 카운트하고 리턴.
        int answer = 0;
        int count = 0;
        
        ArrayList<String> s1List = new ArrayList<>(Arrays.asList(s1));

        for(String s: s2) {
            if (s1List.contains(s)) count++;
        }
        
        answer = count;
        
        return answer;
    }
}