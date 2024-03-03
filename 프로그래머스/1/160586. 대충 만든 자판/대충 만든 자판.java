import java.util.*;
// 대충 만든 자판
class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        // 연속으로 누르면 다음 문자열이 입력되는 자판으로 만들어진 키보드가 있다.
        // 최소 몇번 눌러야 특정 문자열을 작성할 수 있는지 반환하라.
        // 알파벳과, 알파벳의 최소입력을 담은 해시 맵을 만들고 targets으로 계산한 뒤 반환하자.
        int[] answer = new int[targets.length];
        HashMap<String, Integer> map = new HashMap<>();
        
        for(int i = 0; i < keymap.length; i++) {
            for(int j = 0; j < keymap[i].length(); j++) {
                String temp = "" + keymap[i].charAt(j);
                if(map.containsKey(temp)) {
                    if(map.get(temp) > j+1) map.put(temp, j+1);
                } else {
                    map.put(temp, j+1);
                }
            }
        }
        
        for(int i = 0; i < targets.length; i++) {
            for(int j = 0; j < targets[i].length(); j++) {
                String temp = "" + targets[i].charAt(j);
                if(map.containsKey(temp)) {
                    answer[i] += map.get(temp);
                } else {
                    answer[i] = -1;
                    break;
                }
            } 
            if(answer[i] == 0) answer[i] = -1;
        }
        
        return answer;
    }
}