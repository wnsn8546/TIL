import java.util.*;

class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        // board 에서 지뢰 1을 기준으로 위험방향인 8방향을 전부 -1로 바꿔주고 전체에서 0의 개수를 더해준다.
        // 조건문으로 -1로 바꿔줄 인덱스가 해당하는곳이 배열 범위를 벗어나거나, 지뢰가 있던 자리이면 제외한다.
        int [][] direction = {{0, 1},
                              {1, 1},
                              {1, 0},
                              {1, -1},
                              {0, -1},
                              {-1, -1},
                              {-1, 0},
                              {-1,1}};
        
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[i].length; j++) {
                if(board[i][j] == 1) {
                    for(int k = 0; k < direction.length;k++) {
                        if(i+direction[k][0] < board.length && i+direction[k][0] >= 0 &&
                           j+direction[k][1] < board.length && j+direction[k][1] >= 0 && 
                           board[i+direction[k][0]][j+direction[k][1]] != 1) {
                            board[i+direction[k][0]][j+direction[k][1]] = -1;
                        }
                    }
                }
            }
        }

        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] == 0) {
                    answer += 1;
                }
            }
        }
        
        return answer;
    }
}