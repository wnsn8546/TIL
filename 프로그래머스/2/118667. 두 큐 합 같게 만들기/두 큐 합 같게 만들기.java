import java.util.*;
// 두 큐 합 같게 만들기
class Solution {
    public int solution(int[] queue1, int[] queue2) {
        // 길이가 같은 큐 두 개,
        // 하나의 큐를 골라 원소를 추출하고 다른 큐를 넣는 작업을 하면서 두 큐의 합이 같도록할떄 최소 횟수구하기
        int answer = -1;
        
        Queue<Integer> q1 = new LinkedList<Integer>();
        Queue<Integer> q2 = new LinkedList<Integer>();
        
        long sum1 = 0;
        long sum2 = 0;
        int count = 0;
        
        for(int i = 0; i < queue1.length ; i++) {
            q1.offer(queue1[i]);
            sum1 += queue1[i];
            q2.offer(queue2[i]);
            sum2 += queue2[i];
        }
        
        while(count <= queue1.length * 3){
            if(sum1 > sum2){
                int temp = q1.poll();
                sum1 -= temp;
                sum2 += temp;
                q2.offer(temp);
                
            }else if(sum1 < sum2){
                int temp = q2.poll();
                sum2 -= temp;
                sum1 += temp;
                q1.offer(temp);
                
            }else if(sum1 == sum2){
                answer = count;
                break;
            }
            count++;
        }
        
        return answer;
    }
}