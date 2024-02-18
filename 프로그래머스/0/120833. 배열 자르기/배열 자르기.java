// 배열 자르기
class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        // 배열과 정수 두 개가 매개변수로 주어질때 배열의 num1번째 인덱스부터
        // num2번째 인덱스 까지 자른 정 수 배열을 리턴하기
        int[] answer = new int[num2-num1+1];
        int index = 0;
        
        for(int i = num1; i < num2+1; i++) {
            answer[index++] = numbers[i];
        }
        
        return answer;
    }
}