// 모음제거
class Solution {
    public String solution(String my_string) {
        // 주어진 문자열에서 모음을 제거한 문자열을 반환하라.
        String answer = "";
        String[] vowel = {"a", "i", "u", "e", "o"};
        String[] tempStr = my_string.split("");
        
        for(int i = 0; i < tempStr.length; i++) {
            boolean isVowel = false;
            for(int j = 0; j < vowel.length; j++) {
                if(tempStr[i].equals(vowel[j])) isVowel = true;
            }
            if(isVowel == false) answer += tempStr[i];
        }
        
        return answer;
    }
}