
// 평행
class Solution {
    public int solution(int[][] dots) {
        // 두 직선이 평행이 되는 경우가 있으면 1, 없으면 0 리턴하기
        // 평행한다? 기울기가 같다? x차이 분의 y차이
        // 0과1 2와3, 0과2 1과3, 0과3 1과2 기울기 비교해서 한 번이라도 같으면 answer = 1
        int answer = 0;

        double inclination1 = 0;
        double inclination2 = 0;
        double inclination3 = 0;
        double inclination4 = 0;
        double inclination5 = 0;
        double inclination6 = 0;
        
        inclination1 = Math.abs((double)(dots[0][1] - dots[1][1]) / Math.abs(dots[0][0] - dots[1][0]));
        inclination2 = Math.abs((double)(dots[2][1] - dots[3][1]) / Math.abs(dots[2][0] - dots[3][0]));
        
        inclination3 = Math.abs((double)(dots[0][1] - dots[2][1]) / Math.abs(dots[0][0] - dots[2][0]));
        inclination4 = Math.abs((double)(dots[1][1] - dots[3][1]) / Math.abs(dots[1][0] - dots[3][0]));
        
        inclination5 = Math.abs((double)(dots[0][1] - dots[3][1]) / Math.abs(dots[0][0] - dots[3][0]));
        inclination6 = Math.abs((double)(dots[1][1] - dots[2][1]) / Math.abs(dots[1][0] - dots[2][0]));
        
        
        if(inclination1 == inclination2) {
            answer = 1;
        } else if(inclination3 == inclination4) {
            answer = 1;
        } else if(inclination5 == inclination6) {
            answer = 1;
        }
        
        return answer;
    }
}