class Solution {
    public int solution(int[][] lines) {
        // 어떻게 겹치는지 판별할까?
        // 좌표에 그려보면 겹치는지 알 수 있다.
        // 2차원 배열로 -100 ~ 100을 나타내기위해 0~200의 201길이의 배열을 만든다.
        // +100하여 좌표에 해당하는부분은 +1을 해준다.
        // 1을 초과한 경우를 카운트한다.
        int answer = 0;
        int[] coordinate = new int[201];
        
        for(int i = 0; i < lines.length;i++){
            for(int j = lines[i][0]+100 ; j < lines[i][1]+100;j++) {
                coordinate[j] += 1;
            }
        }
        
        for(int c : coordinate){
            if(c > 1) {
                    answer++;
            }
        }
        
        return answer;
    }
}