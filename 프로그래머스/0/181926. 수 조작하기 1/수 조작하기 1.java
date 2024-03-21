class Solution {
    public int solution(int n, String control) {
        int answer = 0;
        
        for(int i = 0; i < control.length();i++) {
            if(control.charAt(i) == 'w'){
                n += 1;
            } else if(control.charAt(i) == 's') {
                n -= 1;
            } else if(control.charAt(i) == 'd') {
                n += 10;
            } else if(control.charAt(i) == 'a') {
                n -= 10;
            }
        }
        
        if(n < -100000) {
            n = -100000;
        } else if(n > 100000) {
            n = 100000;
        }
        answer = n;
        return answer;
    }
}