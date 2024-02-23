// 삼각달팽이
class Solution {
    public int[] solution(int n) {
        // 밑변과 높이가 n인 삼각형에서 삼각달팽이로 채우기...
        // n * n 의 2차원 배열 만들고 삼각형으로 채우기
        int[][] board = new int[n][n]; // 삼각형 채울 2차원배열
        int[] current = {0, 0}; // 시작, 현재위치
        int[] dy = {1, 0, -1}; // 아래로, 오른쪽으로, 왼쪽 위 대각선으로
        int[] dx = {0, 1, -1}; //
        String direction = "down"; // 현재 방향
        int count = 1; // 넣어줄 숫자
        int flagCheck = 0; // 몇 개의 방향이 이미 숫자로 차있는지 확인할 변수.
        
        while(flagCheck < 2) { // 갈 수 없는곳이 2군데 되기전까지 while문 반복.
            board[current[0]][current[1]] = count++; // 현재 위치에 count값을 넣어주고 count++;
            int ny; // 다음 위치의 y좌표
            int nx; // 다음 위치의 x좌표
            
            if(direction.equals("down")){
                ny = current[0] + dy[0];
                nx = current[1] + dx[0];
                
                if(ny < 0 || nx < 0 || ny >= n || nx >= n || board[ny][nx] > 0) { // 벽, 차있는숫자 처럼 못가는 좌표일때는
                    direction = "right"; // 방향을 바꿔주고,
                    flagCheck++; // check 변수에 +1을 해준다.
                    count--; // count를 다시 줄여준다.
                } else {
                    current[0] = ny; // 이동가능하다면, 다음 좌표값으로 바꿔주고,
                    current[1] = nx; //
                    flagCheck = 0; // check변수를 0으로 초기화한다.
                }
            } else if(direction.equals("right")) {
                ny = current[0] + dy[1];
                nx = current[1] + dx[1];
                
                if(ny < 0 || nx < 0 || ny >= n || nx >= n || board[ny][nx] > 0) {
                    direction = "upperleft";
                    flagCheck++;
                    count--;
                } else {
                    current[0] = ny;
                    current[1] = nx;
                    flagCheck = 0;
                }
            } else if(direction.equals("upperleft")) {
                ny = current[0] + dy[2];
                nx = current[1] + dx[2];
                
                if(ny < 0 || nx < 0 || ny >= n || nx >= n || board[ny][nx] > 0) {
                    direction = "down";
                    flagCheck++;
                    count--;
                } else {
                    current[0] = ny;
                    current[1] = nx;
                    flagCheck = 0;
                }
            }
        }
        
        int[] answer = new int[count]; // 카운트 개수만큼의 크기로 answer 배열만들어주고,
        int index = 0; // 몇번째 index인지 확인할 변수
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                 if(board[i][j] != 0) answer[index++] = board[i][j]; // answer에 담아 리턴한다.
            }
        }
        
        return answer;
    }
}