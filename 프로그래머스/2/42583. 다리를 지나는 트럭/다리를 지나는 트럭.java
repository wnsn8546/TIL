import java.util.*;
// 다리를 지나는 트럭
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        // 순서가 정해진 모든 트럭이 다리를 건너려면 최소 몇초가 걸리는지?
        // 다리 길이, 최대 무게, 트럭 무게
        int answer = 0;
        int[] bridge = new int[bridge_length];
        int foreIndex = 0;
        int count = 0;
        
        while (count < truck_weights.length) { // truck_weights.length 개수가 다 건널때까지
            answer++; // 시간 초 추가

            if(bridge[0] > 0) { // 만약 첫번째 값이존재 한다면 0으로 만들어주고 count++
                bridge[0] = 0;
                count++;
            }

            int totalWeight = 0; // 다리 위의 총 무게를 담아놓은 변수
            for(int i = 0; i < bridge_length - 1; i++) { // 자리를 한 개씩 옮겨주고 totalWeight에 추가
                bridge[i] = bridge[i+1];
                bridge[i+1] = 0;
                totalWeight += bridge[i];
            }

            if(bridge[bridge_length - 1] == 0) { // bridge의 마지막 인덱스가 비어있고,
                if(foreIndex < truck_weights.length && totalWeight + truck_weights[foreIndex] <= weight) { // foreIndex가 truck_weights길이보다 짧고, 더해도 최대 무게 보다 작으면
                    bridge[bridge.length - 1] = truck_weights[foreIndex]; // bridge 마지막 칸에 넣어주고
                    foreIndex++; // 인덱스를 올려준다.

                }
            }
        }

        return answer;
    }
}