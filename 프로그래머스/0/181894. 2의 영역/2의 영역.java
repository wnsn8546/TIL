import java.util.*;
 
class Solution {
    public int[] solution(int[] arr) {
        int[] twoIndex = {-1, -1};
        ArrayList<Integer> arrList = new ArrayList<>(); 
        // 2의 시작 인덱스는 twoIndex[0]에, 끝 인덱스는 twoIndex[1]에 넣는다.
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] == 2) {
                if(twoIndex[0] == -1) {
                    twoIndex[0] = i;
                } else {
                    twoIndex[1] = i;
                }
            } 
        }
        // 2 인덱스 개수에 따라 answer 에 답을 넣고 리턴한다.
        if(twoIndex[0] == -1 && twoIndex[1] == -1) {
            int[] answer = {-1};   
            return answer;
        }else if (twoIndex[0] == -1 || twoIndex[1] == -1) {
            int[] answer = {2};
            return answer;
        }else {
            int[] answer = new int[twoIndex[1] - twoIndex[0] + 1];
            for(int i = twoIndex[0]; i <= twoIndex[1] ;i++) {
                arrList.add(arr[i]);
            }
            for(int i = 0; i < answer.length ;i++) {
                answer[i] = arrList.get(i);
            }
            return answer;
        }
        
    }
}