class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        
        for(int h : array) {
            if(height < h) {
                answer++;
            }
        }
        
        
        return answer;
    }
}