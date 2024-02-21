import java.util.*;
// 방문 길이
class Solution {
    public int solution(String dirs) {
        // 캐릭터가 처음 걸어본 길의 길이를 반환하라.
        // 10 * 10 배열을 만들고 시작을 (4,4) 에서부터 움직이면서 지나가는 길을+1씩해주고
        // 이동이 끝나면 1 이상 인곳의 개수만 반환한다.
        // + 이전 좌표와 이후 좌표가 같으면 해시에 값 넣어 놓고 해시 사이즈를 answer로 하자 
        int answer = 0;
        String[] dirsList = dirs.split(""); // dirs 쪼개서 배열로 만들어 놓기
        int[] current = {5,5}; // 시작좌표, 현재좌표가 될 current
        int[][] map = new int [11][11]; // 좌표 맵
        HashMap<String, Integer> linkedHashMap = new LinkedHashMap<>(); // 이전, 지금 길을 담아 놓을 링크드해시맵

        for(int i = 0; i < dirsList.length; i++) { // 방향대로 다음 좌표를 넣어주고, 
            String temp1 = "";
            String temp2 = "";
            int nx = 0;
            int ny = 0;
            if(dirsList[i].equals("U")) {
                ny = current[0] - 1;
                nx = current[1];
            }else if(dirsList[i].equals("D")) {
                ny = current[0] + 1;
                nx = current[1];
            }else if(dirsList[i].equals("L")) {
                ny = current[0];
                nx = current[1] - 1;
            }else if(dirsList[i].equals("R")) {
                ny = current[0];
                nx = current[1] + 1;
            }

            if(nx < 0 || ny < 0 || nx > 10 || ny > 10){ // 좌표 밖 범위이면 continue, 
                continue;
            }

            // temp1, 거꾸로인 2에 이전, 현재 좌표 정보를 문자열로 담아서,
            temp1 = Integer.toString(current[0]) + Integer.toString(current[1]) +
                Integer.toString(ny) + Integer.toString(nx);
            temp2 = Integer.toString(ny) + Integer.toString(nx) + Integer.toString(current[0]) +
                Integer.toString(current[1]);
            
            // 새로운 길이면, 링크드 해시맵에 넣는다.
            if(!(linkedHashMap.containsKey(temp1)) && !(linkedHashMap.containsKey(temp2))) {
                linkedHashMap.put(temp1, 1);
            }
            
            current[0] = ny; // 다음 좌표를 현재 좌표로 바꾼다.
            current[1] = nx;
        }

        answer = linkedHashMap.size(); // 링크드 해시맵의 사이즈를 리턴한다.
        
        return answer;
    }
}