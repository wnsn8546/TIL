import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        // 정수배열 number에서 서로 다른 인덱스의 두 수를 뽑아 더해서 만들 수 있는 모든 수를
        // 배열에 담아 오름차순으로 리턴하기
        int[] answer = {};
        ArrayList<Integer> arrNumbers = new ArrayList<>();
        
        for(int i = 0; i < numbers.length-1; i++) {
            for(int j = i + 1; j < numbers.length; j++) {
                if(!(arrNumbers.contains(numbers[i] + numbers[j]))) {
                    arrNumbers.add(numbers[i] + numbers[j]);
                }
            }
        }
        Collections.sort(arrNumbers);
        
        answer = new int[arrNumbers.size()];
        for(int i = 0; i < arrNumbers.size(); i++) {
            answer[i] = arrNumbers.get(i);
        }
        
        return answer;
    }
}