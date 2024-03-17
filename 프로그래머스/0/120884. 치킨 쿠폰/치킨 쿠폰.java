class Solution {
    public int solution(int chicken) {
        int answer = 0;
        int coupon = chicken;
        int service = 0;
            
        while(coupon >= 10) {
            answer += coupon / 10;
            service = coupon / 10;
            coupon = service + coupon % 10;
        }
        
        return answer;
    }
}