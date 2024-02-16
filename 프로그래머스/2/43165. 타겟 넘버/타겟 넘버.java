import java.util.*;
// 타겟 넘버
class Solution {
    public int solution(int[] numbers, int target) {
        // 타겟 넘버를 만들 수 있는 경우의 수 구하기
        // 모든 경우에서 타겟넘버가 만들어질때 마다 answer에 +1 해주기
        // +일 경우, -일 경우 모든 경우를 큐를 이용해서 BFS? 완전 탐색
        
        int answer = 0;
        int start = 0; // 0으로 시작한다.
        
        Queue<Integer> q = new LinkedList<>(); // 큐를 만든다.
        q.offer(start); // 0을 큐에 넣고,
        
        for (int num : numbers) { // numbers를 순회하면서
            int qSize = q.size(); // 큐 사이즈를 담아놓고,
            for (int i = 0; i < qSize; i++) { // 큐 사이즈 만큼 반복
                int poll = q.poll(); // 꺼내고
                
                q.offer(poll + num); // 현재 num의 값을 더했을때의 값과
                q.offer(poll - num); // 뺐을때의 값을 넣어준다.
            }
        }
        
        while (!q.isEmpty()) { // 모든 경우의 결과가 넣어진 큐가 빌때까지 
            int poll = q.poll(); // 하나하나 꺼낸다
            
            if (poll == target) { // 꺼낸값이 타겟 넘버랑 같으면 answer++
                answer++;
            }
        }
        
        return answer;
    }
}