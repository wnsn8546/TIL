import java.util.*;
// 기능개발
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> dayInfo = new ArrayList<>();
        int completedCount = 0;

        while(completedCount != progresses.length) {
            int temp = completedCount;
            for(int i = completedCount; i < progresses.length; i++) {
                progresses[i] += speeds[i];
            }
            for(int i = temp; i < progresses.length; i++) {
                if(progresses[completedCount] < 100) {
                    break;
                }
                else {
                    if(progresses[i] >= 100) {
                        completedCount++;
                    }
                }
            }

            if(completedCount-temp != 0) dayInfo.add(completedCount-temp);

        }
        
        int[] answer = new int[dayInfo.size()];
        for(int i = 0; i < dayInfo.size(); i++) {
            answer[i] = dayInfo.get(i);
        }

        return answer;
    }
}