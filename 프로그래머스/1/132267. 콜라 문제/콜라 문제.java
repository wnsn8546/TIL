// 콜라 문제
class Solution {
    public int solution(int a, int b, int n) {
        // a개를 주면 b병을 주는 마트가 있을때 n병이면 얼마를 받을 수 있나
        int answer = 0;
        int namuji = 0;
        
        while (n >= a) {
            namuji = n % a;
            answer += (n / a) * b;
            n = (n / a) * b + namuji;
        }
        
        return answer;
    }
}