class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int count = 1; // 현재 채워넣을 숫자
        int i = 0; // 행
        int j = 0; // 열
        String direction = "right"; // 오른쪽 시작, 현재 진행방향.
        // n*n 숫자까지 채우기 위해 while 문으로 반복한다.
        // 진행하면서 배열 범위를 넘어가거나, 이미 다른 숫자가 채워져 있는 경우 
        // 해당 방향으로 진행하지 못하기 때문에,
        // 조건문으로 방향을 시계방향으로 바꿔준다.
        while (count <= (n*n)) {
            answer[i][j] = count;
            
            if(direction.equals("right")) {
                if(j == (n-1) || answer[i][j+1] != 0) {
                    direction = "down";
                    i++;
                } else {
                    j++;
                }
            } else if (direction.equals("down")) {
                if(i == (n-1) || answer[i+1][j] != 0) {
                    direction = "left";
                    j--;
                } else {
                    i++;
                }
            } else if (direction.equals("left")) {
                if(j == 0 || answer[i][j-1] != 0) {
                    direction = "up";
                    i--;
                } else {
                    j--;
                }
            } else {
                if(i == 0 || answer[i-1][j] != 0) {
                    direction = "right";
                    j++;
                } else {
                    i--;
                }
            }
            count++;
        }
        
        return answer;
    }
}