import java.util.Stack;
// 햄버거 만들기
class Solution {
    public int solution(int[] ingredient) {
        // 빵1 - 야채2 - 고기3 - 빵1
        // 스택으로
        // 1,2,3,1 이 나오면 해당 부분을 빼고 그 전 인덱스부터 다시.
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        String hamburger = "1231";
        
        for(int i = 0; i < ingredient.length; i++) {
            stack.push(ingredient[i]);
            if(stack.size() >= 4) {
                if(stack.get(stack.size()-4) == 1 && stack.get(stack.size()-3) == 2 && stack.get(stack.size()-2) == 3 && stack.get(stack.size()-1) == 1) {
                    stack.pop();
                    stack.pop();
                    stack.pop();
                    stack.pop();
                    answer++;
                }
            }
        }

        return answer;
    }
}