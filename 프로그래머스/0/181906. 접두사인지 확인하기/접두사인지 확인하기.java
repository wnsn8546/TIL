class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 0;
        // startsWith를 사용해서 접두사인지 확인
        if(my_string.startsWith(is_prefix)){
            answer = 1; 
        }
         
        return answer;
    }
}