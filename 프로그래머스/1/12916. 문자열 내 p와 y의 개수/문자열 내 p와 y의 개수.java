// 문자열 내 p와 y의개수
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int pCount = 0; // p의 개수를 담을 변수
        int yCount = 0; // y의 개수를 담을 변수
        
        s = s.toLowerCase(); // 모두 소문자로 먼저 바꿔 놓고,
        String[] splitString = s.split(""); // 쪼개놓는다.
        for(String c : splitString) { // 문자열 순회하면서 count를 올려준다.
            if(c.equals("p")){ 
                pCount++;
            }
            if(c.equals("y")){
                yCount++;
            }
        }
        if(pCount != yCount){ // 같지 않으면 false로 바꿔서 리턴해준다.
            answer = false;
        }

        return answer;
    }
}