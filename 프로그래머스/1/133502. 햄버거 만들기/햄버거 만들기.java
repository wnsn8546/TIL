import java.util.*;
// 햄버거 만들기
class Solution {
    public int solution(int[] ingredient) {
        // 빵1 - 야채2 - 고기3 - 빵1
        int answer = 0;
        String hamburger = "1231";
        String ingredientStr = Arrays.toString(ingredient).replaceAll("[^0-9]", "");
        
        while (true) {
            int beforeLength = ingredientStr.length();
            ingredientStr = ingredientStr.replaceFirst("1231", "");
            int afterLength = ingredientStr.length();
            
            if(beforeLength == afterLength) {
                break;
            } else {
                answer++;
            }
        }

        return answer;
    }
}