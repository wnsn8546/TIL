import java.util.*;
// 실패율
class Solution {
    public int[] solution(int N, int[] stages) {
        // 실패율 = 스테이지에 도달했으나 아직클리어 하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
        // 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담긴 배열을 리턴하라.
        // N = 스테이지 개수, stages = 플레이어들이 현재 도전중인 스테이지
        // 실패율 = 해당 스테이지에 멈춰있는 사람 / 해당 스테이지 이상 숫자를 가진 사람
        // 을 내림차순으로 정렬해서 리턴
        // 길이 20만개
        // 배열의 길이 N, N은 500이하
        int[] nowStage = new int[N + 1]; // 현재 도달한 스테이지
        int[] clearedNum = new int[N + 1]; // 스테이지별 클리어한 사람 수를 담을 배열
        HashMap<Integer, Double> map = new HashMap<>(); // 스테이지 번호와, 실패율을 저장할 해시맵

        for (int i = 0; i < stages.length; i++) { // stages 배열을 순회하면서,
            nowStage[stages[i] - 1] += 1; // 아직 클리어하지 못한사람배열에 +1 해주고,
            for (int j = 0; j < stages[i]; j++) { 
                clearedNum[j] += 1; // 도달한 스테이지 전까지 스테이지를 클리어한 사람 수에 +1해준다.
            }
        }
        
        for (int i = 0; i < N; i++) { // 실패율 계산해서 맵에 저장하기
            if (nowStage[i] == 0 || clearedNum[i] == 0) { // 스테이지에 도달한 사람이 없거나, 클리어한 사람이 없을때는
                map.put(i + 1, 0.0); // 실패율 0이 안들어가니 0.0으로 넣어준다.
            } else {
                map.put(i + 1, (double) nowStage[i] / (double) clearedNum[i]);
            }
        }

        ArrayList<Integer> failureRateList = new ArrayList<>(map.keySet()); // 해시맵 밸류순으로 내림차순 정렬하기
        failureRateList.sort((o1, o2) -> Double.compare(map.get(o2), map.get(o1)));

        int[] answer = new int[failureRateList.size()]; // answer 배열을 실패율리스트 길이 만큼 만들고,
        
        for(int i = 0; i < failureRateList.size(); i++) { // 담아서 리턴한다.
            answer[i] = failureRateList.get(i); 
        }
        
        return answer;
    }
}