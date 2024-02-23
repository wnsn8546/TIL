import java.util.*;
// 최빈값 구하기
class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int[] temp = new int[1000];
        int max = -1;
        int count = 0;
        // 수가 적으므로 1000개 배열로 풀이
        // 숫자가 나타날때마다 임시 배열의 해당하는 인덱스의 값에 +1을 해준다.
        for(int i = 0; i < array.length;i++) {
            temp[array[i]] += 1; 
        }
        // 최대빈도수를 체크하고, 인덱스를 answer에 담아놓는다.
        for(int i = 0; i < temp.length;i++) {
            if(temp[i] > max) {
                max = temp[i];
                answer = i;
             }
        }
        // 최빈값과 같은 값이 몇개 있는지 체크하고 count가 2이상이 되면 -1을 리턴한다.
        for(int i = 0; i < temp.length;i++) {
            if(temp[i] == max){
                count++;
                if(count > 1) {
                    answer = -1;
                    return answer;
                }
            }
        }

        return answer;
    }
}