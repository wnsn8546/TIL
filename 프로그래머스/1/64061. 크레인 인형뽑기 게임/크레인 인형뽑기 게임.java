import java.util.*;
// 크레인 인형뽑기 게임
class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> basket = new Stack<>();

        for(int m = 0 ; m < moves.length; m++) {
            for(int i = 0 ; i < board.length; i++) {
                int temp = board[i][moves[m]-1];
                if(board[i][moves[m]-1] > 0) {
                        if(basket.size() != 0 && basket.peek() == board[i][moves[m]-1]) {
                            basket.pop();
                            board[i][moves[m]-1] = 0;
                            answer += 2;
                        } else {
                            basket.push(board[i][moves[m]-1]);
                            board[i][moves[m]-1] = 0;
                        }
                    break;
                }
            }
        }
        
        return answer;
    }
}