class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];        
        // 2중 for문으로 현재 값이 다른 요소들 보다 작을때 마다 +1등을 해줘서 몇등인지를 배열에 담는다.
        for(int i = 0; i < emergency.length; i ++) {
            int rank = 1;
            for(int j = 0; j < emergency.length; j ++) {
                if (emergency[i] < emergency[j]) {
                    rank += 1;
                }
            }
            answer[i] = rank;
        }
        
        return answer;
    }
}