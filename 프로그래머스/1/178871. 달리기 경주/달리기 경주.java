import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = new String[players.length];
        // 해설진이 선수의 이름을 부를 경우, 불려진 선수와 앞선 선수의 위치가 바뀐다.
        // 불려진 선수의 인덱스를 구해놓고, 임시변수를 사용해서 값을 바꾼다.
        // 4개 시간초과? 자리바꾸는데에 복잡도가 올라가는걸까?
        // 배열의 탐색 속도가 O(n)이라 탐색에만 최대 5만 * 100만 이상의 시간이 소요되는것 같다?
        // 그러면 맵으로 등수와 같이 저장해놓고 불려진 선수를 탐색하면 빨라질것같다.
        // HashMap의 탐색 속도는 O(1)이기 떄문에. 파이썬의 딕셔너리와 같다.
        // 맵만 사용해서 구현하는데 계속 막히는 부분이 생겼다... 
        // 해시에서는 불려진 선수의 이름으로 등수를 찾은 다음,
        // 배열에서 불려지는 순간마다 바로바로 앞선수와의 등수와 자리를 교체해주면 될것 같다.
        // 시간복잡도 O(m+n)?
        HashMap<String, Integer> rank = new HashMap<>();
        // 맵에 현재 등수와 함께 넣어준다.
        for(int i = 0; i < players.length; i++) {
            rank.put(players[i], i);
        }
        // callings 배열을 순회하면서
        for(int i = 0; i < callings.length; i++) {
            // 불려진 선수의 현재등수를 맵에서 찾고
            int calledRank = rank.get(callings[i]);
            // 앞선수의 이름을 저장해놓고
            String frontPlayer = players[calledRank-1];
            // 등수와 자리를 바꿔준다.
            rank.put(frontPlayer, calledRank); // 앞 선수는 불려진 선수 등수로
            rank.put(callings[i], calledRank-1); // 불려진 선수 등수 -1
            players[calledRank] = frontPlayer; // 불려진 선수 자리로 앞선수 이동
            players[calledRank-1] = callings[i]; // 앞선수 자리로 불려진 선수 이동
        }
        
        return players;
    }
}