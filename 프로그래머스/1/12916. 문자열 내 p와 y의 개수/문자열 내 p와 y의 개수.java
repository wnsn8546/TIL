// 문자열 내 p와 y의개수
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int pNum = 0;
        int yNum = 0;
        
        s = s.toLowerCase();
        String[] splitString = s.split("");
        for(String c : splitString) {
            if(c.equals("p")){
                pNum++;
            }
            if(c.equals("y")){
                yNum++;
            }
        }
        if(pNum != yNum){
            answer = false;
        }

        return answer;
    }
}