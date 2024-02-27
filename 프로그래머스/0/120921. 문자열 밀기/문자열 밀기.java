import java.util.*;
// 문자열 밀기
class Solution {
    public int solution(String A, String B) {
        // hello
        // 문자열 A와 B가 매개변수로 주어질때, A를 밀어서 B가 될 수 있는 최소  횟수를 리턴한고,
        // B가 될 수 없으면 -1을 리턴하라.
        // A의 첫번째 인덱스의 알파벳이 B에서 몇번째 있는지를 찾고, 차이 만큼 옮긴 문자열을 만들었을때,\
        // 일치하는지 안하는지 리턴하자.
        // 첫번째 아이디어 예외발견, 그냥 계속 만들면서 비교해보자.
        int answer = -1;
        String[] aArr =  A.split("");
        String[] bArr =  B.split("");
        int length = aArr.length;
        
        for(int i = 1; i < length+1 ;i++) {
            String newStr = "";
             for(int j = length-i ; j < length-i + length ; j++) {
                 newStr += aArr[j % length];
             }
            if(newStr.equals(B)) {
                answer = i;
                break;
            }
        }
        
        if(answer == length) answer = 0;
        
        return answer;
    }
}