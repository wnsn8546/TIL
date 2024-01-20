import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        List<Integer> queue = new LinkedList<>();
        int target = priorities[location];
        priorities[location] = 0;
        
        for (int n : priorities) {
            queue.add(n);
        }
        
        while (!queue.isEmpty()) {
            int now = queue.remove(0);
            int check = 0;
            
            for (int i = 0; i < queue.size(); i++) {
                if (now == 0) {
                    if (target < queue.get(i)) {
                        queue.add(now); check = 1; break;
                    } else continue;
                } else if (queue.get(i) == 0 && now < target) {
                    queue.add(now); check = 1; break;
                } else if (now < queue.get(i)) {
                    queue.add(now); check = 1; break;
                }
            }
            
            if (check == 0 && now == 0) return answer;
            if (check == 0) answer++;
            
        }
        
        return answer;
    }
}