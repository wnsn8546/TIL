class Solution {
    public int solution(int n) {
        int answer = 0;
        int slice = 7;
        int mod = 0;
        
        answer = n / slice;
        mod = n % slice;
        
        if(mod > 0) answer++;
           
        return answer;
    }
}