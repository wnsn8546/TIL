class Solution {
    public int solution(int n) {
        int answer = 0;
        double temp = Math.sqrt(n);
        
        if((temp - (int) temp) > 0) {
            answer = 2;
        } else {
            answer = 1;
        }
        
        return answer;
    }
}