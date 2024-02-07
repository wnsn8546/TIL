//import java.util.*;

class Solution {
    
    public int solution(String my_string) {
        // 하나하나 숫자인지를 판별한다
        // 숫자들을 더해준다.
        // X
        // 알파벳을 먼저 공백으로 바꿔준다.
        // 공백을 구분자로 다시 split한다.
        // 숫자문자열을 정수로 바꿔서 더해준다.
        int answer = 0;
        // split을 사용해서 배열로 만든다.
        String[] sArr = my_string.split("");
        // 숫자는 숫자, 숫자가 아닌경우에 " "로, 새로운 문자열에 더해준다.
        String newString = "";
        for(int i = 0; i < sArr.length; i++) {
            if(!isNumber(sArr[i])) {
                newString += " ";
            }else {
                newString += sArr[i];
            }
        }
        //공백을 기준으로 숫자문자열를 담은 리스트를 만들고
        String[] numArr = newString.split(" ");
        //숫자 문자열을 answer에 더해준다.
        for(String s : numArr) {
            if(isNumber(s)) {
                answer += Integer.parseInt(s);
            }
        }
        
        return answer;
    }
    
    // 숫자면 true 문자면 false를 반환해줄 함수.
    public static boolean isNumber(String s) {
            try {
                Integer.parseInt(s);
            } catch (NumberFormatException e) {
                return false;
            }
            
            return true;
    }
}