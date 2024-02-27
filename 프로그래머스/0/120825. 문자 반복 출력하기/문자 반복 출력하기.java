// 문자 반복 출력하기
class Solution {
    public String solution(String my_string, int n) {
        // my_string에 있는 각 문자를 n번 반복한 문자열을 리턴하기.
        String answer = "";
        
        for(int i = 0; i < my_string.length(); i++) {
            for(int j = 0; j < n; j++) {
                answer += my_string.charAt(i);
            }
        }
                
        return answer;
    }
}