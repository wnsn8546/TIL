// 양꼬치
class Solution {
    public int solution(int n, int k) {
        // 10인분을 먹으면 음료수 하나를 서비스로
        // 양꼬치는 1인분에 12,000원, 음료수는 2,000원
        // 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return
        int answer = 0;
        
        answer += n * 12000 + (k - n/10)* 2000; 
        
        return answer;
    }
}