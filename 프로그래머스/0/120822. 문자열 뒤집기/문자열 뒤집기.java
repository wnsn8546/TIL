class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] split =  my_string.split("");
        
        for (int i = split.length-1 ; i >= 0 ;i--) {
            answer += split[i];
        }
        
        return answer;
    }
}