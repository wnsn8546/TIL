import java.util.*;
 
class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int answer = 0;
        int a = 0;
        int b = 0;
        int c = 0;
        // rank 값과 인덱스를 같이 저장해놓을 HashMap
        HashMap<Integer, Integer> map = new HashMap<>();
        // HashMap에 넣어두기
        for(int i = 0; i < rank.length; i++) {
            map.put(rank[i], i);
        } 
        // 참석하는 인원들의 rank 값을 담아 놓을 ArrayList
        ArrayList<Integer> arrList = new ArrayList<>();
        // 참석하는 인원이면 ArrayList에 넣기
        for(int i = 0; i < rank.length ; i++) {
            if(attendance[i] == true) {
                arrList.add(rank[i]);
            }
        }
        // 등수 순으로 정렬
        Collections.sort(arrList);
        // HashMap에서 등수 순으로 등수를 key값으로 value-인덱스를 꺼내서  a, b, c 에 넣는다. 
        a = map.get(arrList.get(0));
        b = map.get(arrList.get(1));
        c = map.get(arrList.get(2));

        // answer를 계산하고 리턴한다.
        answer = 10000 * a + 100 * b + c;

        return answer;
    }
}