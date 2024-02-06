import java.util.*;

class Solution {
    public int[] solution(String myString) {
        String[] split = myString.split("");
        ArrayList<Integer> arrList = new ArrayList<>();
        int count = 0;
        // x가 나오기 전까지 문자열의 기준을 계산해서 arrList에 넣는다.
        for(int i = 0; i < myString.length(); i++){
            if (split[i].equals("x")) {
                arrList.add(count);
                count = 0;
            } else {
                count += 1;
            }
        }
        arrList.add(count);
        // arrList를 int[] answer에 넣고 리턴한다.
        int[] answer = new int[arrList.size()];
        for(int i = 0; i < arrList.size(); i++) {
            answer[i] = arrList.get(i);
        }
        
        
        return answer;
    }
}