class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        int count = 0;
        
        while(count < n) {
            if(count == 0) {
                answer[0] = x;
            } else {
                answer[count] = answer[count-1] + x;
            }
            count++;
        }
        
        
        return answer;
    }
}