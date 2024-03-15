import java.util.*;
// 택배상자
class Solution {
    public int solution(int[] order) {
        // 증가하는 순서대로 컨테이너 벨트에 놓여 영재에게 전달된다.
        // 택배기사님이 원하는 순서가 주어졌을때, 보조 컨테이너 벨트를 사용하여
        // 몇개의 상자를 실을 수 있나
        int answer = 0;
        Stack<Integer> assistantBelt = new Stack<>();
        List<Integer> truck = new ArrayList<>(); 
        int count = 0;

        for(int i = 1; i < order.length + 1 ; i++) {
            if(i != order[count]) {
                assistantBelt.push(i);
            } else {
                truck.add(i);
                count++;
            }
            while(assistantBelt.size() != 0) {
                if(assistantBelt.peek() == order[count]) {
                    truck.add(assistantBelt.pop());
                    count++;
                } else {
                    break;
                }
            }
        }
        
        answer = truck.size();
        
        return answer;
    }
}