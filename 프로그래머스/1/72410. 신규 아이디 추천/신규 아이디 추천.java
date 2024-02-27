import java.util.*;
// 신규 아이디 추천
class Solution {
    public String solution(String new_id) {
        // 규칙에 맞지 않는 아이디를 입력했을때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디 추천하기.
        // 순서대로하기.
        String answer = "";
        String tempNewId = "";
        
        tempNewId = changeToLower(new_id); // 소문자로 치환
        tempNewId = removeCharactors(tempNewId); // 특정 문자("소문자", "숫자", "-", "_",".") 제외한 모든 문자 제거
        tempNewId = checkDoubleDot(tempNewId); // 연속된 ".." 을 "."으로 치환
        tempNewId = checkDotLocation(tempNewId); // "."가 처음이나 끝에 위치해 있을 때 제거.
        tempNewId = checkEmpty(tempNewId); // 빈 문자열이라면 "a"를 대입 하기
        tempNewId = checkLength(tempNewId); // 길이가 16자 이상이면 15개 문자 제외하고 나머지를 제거. 만약 마침표가 끝에 위치한다면 "."을 제거
        tempNewId = checkDotLocation(tempNewId);
        tempNewId = check2Length(tempNewId); // 길이가 2자 이하라면, 마지막 문자를 문자길이가 3이 될때까지 반복.
        
        
        System.out.println(tempNewId);
        answer = tempNewId;
        
        return answer;
    }
    
    public static String changeToLower (String new_id) {
        return new_id.toLowerCase();
    }
    
    public static String removeCharactors (String tempNewId) {
        String temp = "";
        
        for (int i = 0; i < tempNewId.length(); i++) {
            if ((tempNewId.charAt(i) >= 'a' && tempNewId.charAt(i) <= 'z') || (tempNewId.charAt(i) >= '0' && tempNewId.charAt(i) <= '9') || tempNewId.charAt(i) == '-' || tempNewId.charAt(i) == '_' || tempNewId.charAt(i) == '.') {
                temp += tempNewId.charAt(i);
            }
        }
        return temp;
    }
    
    public static String checkDoubleDot (String tempNewId) {
        while (tempNewId.contains("..")) {
            tempNewId = tempNewId.replace("..", ".");
        }
        
        return tempNewId;
    }
    
    public static String checkDotLocation (String tempNewId) {
        
        if (tempNewId.length() > 0) {
            if (tempNewId.charAt(0) == '.') {
                tempNewId = tempNewId.substring(1, tempNewId.length());
            }
        }
        
        if (tempNewId.length() > 0) {
            if (tempNewId.charAt(tempNewId.length() - 1) == '.') {
                tempNewId = tempNewId.substring(0, tempNewId.length() - 1);
            }
        }
        return tempNewId;
    }
    
    public static String checkEmpty (String tempNewId) {
        if( tempNewId.equals("")) tempNewId = "a";
        return tempNewId;
    }
    
    public static String checkLength (String tempNewId) {
        if(tempNewId.length() <= 15) {
            return tempNewId;
        } else {
            String[] temp1 = tempNewId.split("");
            tempNewId = "";
            for(int i = 0; i < 15; i++) {
                tempNewId += temp1[i];
            }
            return tempNewId;
        }
    }
    
    public static String check2Length (String tempNewId) {
        if(tempNewId.length() <= 2) {
            String temp = "";
            String str = "" + tempNewId.charAt(tempNewId.length()-1);

            while(tempNewId.length() < 3){
                tempNewId += str;
            }
        }
        return tempNewId;
    }
}