class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] splited =  my_string.split("");
        
        for (int i = splited.length-1 ; i >= 0 ;i--) {
            answer += splited[i];
        }
        
        return answer;
    }
}