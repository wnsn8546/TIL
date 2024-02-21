import java.util.*;
// 나누어 떨어지는 숫자 배열
class Solution {
    public int[] solution(int[] arr, int divisor) {
        // 배열의 각 원소 중 divisor 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하라.
        ArrayList<Integer> tempList = new ArrayList<>();
        
        for(int i = 0; i < arr.length; i++){ // 나누어 떨어지는 숫자를 tempList에 추가해놓고,
            if(arr[i] % divisor == 0){
                tempList.add(arr[i]);
            }
        }
        
        if(tempList.size() == 0) { // 나누어 떨어지는 수가 없으면 -1를 리턴,
            int[] answer = {-1};
            return answer;
        }else { // 있을때는 answer 배열에 넣어서 리턴.
            int[] answer = new int[tempList.size()];
        
            for(int i = 0; i < tempList.size(); i++){
                answer[i] = (int) tempList.get(i);
            }
            Arrays.sort(answer);
            return answer;
        }
    }
}