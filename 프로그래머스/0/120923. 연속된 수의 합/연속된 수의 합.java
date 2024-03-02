// 연속된 수의 합
class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        int nCount = num;
        int plusCount = (num-1) * (num-1 + 1) / 2;
        int startNum = (total - plusCount) / nCount;
        
        for(int i = 0; i < num; i++) {
            answer[i] = startNum + i;
        }
        
        return answer;
    }
}