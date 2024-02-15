import java.util.*;

class Solution {
    public String solution(String s, int n) {
        // 문자열 다 담아 놓고 인덱스 n씩 더해한 문자열로 리턴한다.
        String[] sList = s.split("");
        String[] alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
        
        String answer = "";
        for(String c : sList) {
            char cTemp = c.charAt(0);
            if(Character.isUpperCase(cTemp)) { // 대문자 일때
                String temp = Character.toString(Character.toLowerCase(cTemp));
                
                for(int i = 0;i < alphabet.length ;i++) {
                    if(alphabet[i].equals(temp)) {
                        answer += alphabet[(i+n) % 26].toUpperCase(); 
                    }
                }
            } else if(c.equals(" ")) {
                answer += " ";
            } else { // 소문자 일때
                for(int i = 0;i < alphabet.length ;i++) {
                    if(alphabet[i].equals(c)) {
                        answer += alphabet[(i+n) % 26]; 
                    }
                }
            }
        }
        
        return answer;
    }
}