import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        // 사진별로 추억 점수. 
        // 인물의 그리움점수를 모두 합산한 값이 해당 사진의 추억점수.
        // 해시맵에 name, yearning을 기록해 놓고 photo 2차원배열을 순회한다.
        HashMap<String, Integer> map = new HashMap<>();
        // 해시맵에 이름, 점수쌍을 넣는다.
        for(int i = 0;i < name.length ;i++) {
            map.put(name[i], yearning[i]);
        }
        // photo 배열을 순회하면서 점수를 더해준다.
        // null값이 아닐경우에만
        for(int i = 0;i < photo.length ;i++) {
            for(int j = 0;j < photo[i].length ;j++) {
                if(map.get(photo[i][j]) != null) {
                    answer[i] += map.get(photo[i][j]);
                }
            }
        }
        
        return answer;
    }
}