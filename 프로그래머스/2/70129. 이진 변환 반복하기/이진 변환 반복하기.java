// 이진 변환 반복하기
class Solution {
    public int[] solution(String s) {
        // 0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환
        // 모든 0을 제거한 x의 길이를 c라고할때, c를 2진수로 바꾸어서 리턴하라.
        int[] answer = new int[2];
        String tempStr1 = s; // s를 담고, 2진변환한 수를 계속 저장할 변수.
        int countChange = 0; // 변환 개수
        int countRemoveZero = 0; // 0제거 개수
        
        while(tempStr1.length() != 1) { // 길이가 1될때까지 반복.
            countChange++;
            String tempStr2 = "";
            char[] cArr = tempStr1.toCharArray();
            for(int i = tempStr1.length() - 1; i >= 0; i--) { // 0제거, 1새로운 문자열에 추가.
                if(cArr[i] == '1') {
                    tempStr2 += "1";
                } else {
                    countRemoveZero++; 
                }
            }
            
            // 이진변환
            int length = tempStr2.length();
            tempStr1 = "";
            while (length != 0) {
                tempStr1 += length % 2;
                length /= 2;
            }
        }
        answer[0] = countChange;
        answer[1] = countRemoveZero;
        
        return answer;
    }
}