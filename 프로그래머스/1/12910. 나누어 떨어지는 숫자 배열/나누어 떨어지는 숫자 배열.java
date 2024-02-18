import java.util.*;
// 나누어 떨어지는 숫자 배열
class Solution {
    public int[] solution(int[] arr, int divisor) {
        // 배열의 각 원소 중 divisor 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하라.
        int count = 0;
        int number = 0;
        
        for(int i = 0; i < arr.length; i++){
            if(arr[i] % divisor == 0){
                count++;
            }
        }
        
        if(count == 0){
            int[] answer = {-1};
            return answer;
        }
        
        int[] answer = new int[count];
        
        for(int i = 0; i < arr.length; i++){
            if(arr[i] % divisor == 0){
                answer[number] = arr[i];
                number++;
            }
        }
        
        Arrays.sort(answer);
        return answer;
        
    }
}