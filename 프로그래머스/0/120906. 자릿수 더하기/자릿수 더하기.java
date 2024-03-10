class Solution {
    public int solution(int n) {
        int answer = 0;
        String[] numStr = Integer.toString(n).split("");
        
        for(int i = 0; i < numStr.length; i++) {
            answer += Integer.parseInt(numStr[i]);
        }
        
        return answer;
    }
}