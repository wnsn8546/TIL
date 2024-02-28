import java.util.*;
// 문자열 압축
class Solution {
    public int solution(String s) {
        // 입출력할 문자열 s를 1개 이상 문자열을 잘라 압축하여 표현한것중 가장 짧은 것의 길이를 반환하라.
        int answer = 0;
        String[] compArr = new String[s.length()+1]; // 각 길이 만큼 압축했을때의 결과를 담아 놓을 문자열배열.
        int min = 1001; // s길이 범위 +1;

        for(int i = 1; i < s.length()+1; i++) {
            String tempStr = "";
            int count = 1;
            int j = i;

            while(j < s.length()-i+1) {
                String t1 = s.substring(j,j+i);
                String t2 = s.substring(j-i, j-i+i);
                if(s.substring(j,j+i).equals(s.substring(j-i, j-i+i))) {
                    count++;
                } else {
                    tempStr += s.substring(j-i, j-i+i);
                    if(count > 1) {
                        tempStr += Integer.toString(count);
                        count = 1;
                    }
                }
                j += i;
            }
            tempStr += s.substring(j-i, s.length());
            if(count > 1) {
                tempStr += Integer.toString(count);
                count = 1;
            }

            if(tempStr.length() < min && j-i <= s.length() - 1)  min = tempStr.length();
        }
        answer = min;
        return answer;
    }
}