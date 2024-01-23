import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        int start = 0;
        
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        
        for (int num : numbers) {
            int len = queue.size();
            
            for (int i = 0; i < len; i++) {
                int pop = queue.remove();
                
                queue.add(pop + num);
                queue.add(pop - num);
            }
        }
        
        while (!queue.isEmpty()) {
            int pop = queue.remove();
            
            if (pop == target) {
                answer++;
            }
        }
        
        
        return answer;
    }
}