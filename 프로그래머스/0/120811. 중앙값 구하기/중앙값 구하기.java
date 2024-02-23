import java.util.*;
// 중앙값 구하기
class Solution {
    public int solution(int[] array) {
        // 정렬 후 length / 2 인덱스값 리턴하기
        int answer = 0;
        
        Arrays.sort(array);
        
        answer = array[array.length / 2];
        
        return answer;
    }
}