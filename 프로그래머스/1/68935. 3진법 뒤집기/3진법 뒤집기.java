// 3진법 뒤집기
class Solution {
    public int solution(int n) {
        // 3진법 수를 만든 후, parseInt를 해준다.
        int answer = 0;
        String temp = "";
        
        while (n != 0) {
            temp += n % 3;
            n /= 3;
        }
        
        answer = Integer.parseInt(temp, 3);
        
        return answer;
    }
}