import java.util.Stack;
// 뒤에 있는 큰 수 찾기
class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Stack<Integer> stack = new Stack<>();

        for(int i = 0; i < answer.length; i++) {
            if(stack.size() == 0) {
                stack.push(numbers[i]);
                answer[i] = -1;
            } else {
                int count = 1;
                while(stack.size() != 0) {
                    if(stack.peek() < numbers[i]){
                        if(answer[i- count] == -1){
                            stack.pop();
                            answer[i - count] = numbers[i];
                            count++;
                        } else {
                            count++;
                        }
                    } else {
                        break;
                    }
                }
                stack.push(numbers[i]);
                answer[i] = -1;
            }
        }

        return answer;
    }
}