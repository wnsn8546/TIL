class Solution {
    public int solution(int slice, int n) {
        int answer = 0;
        int mod = 0;
        
        answer = n / slice;
        mod = n % slice;
        
        if(mod > 0) answer++;
        
        return answer;
    }
}