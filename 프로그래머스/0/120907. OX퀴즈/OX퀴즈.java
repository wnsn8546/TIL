class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        String[][] quizArr = new String[quiz.length][5];

        for(int i = 0; i < quiz.length;i++ ) {
            quizArr[i] = quiz[i].split(" ");
        }
        
        for(int i = 0; i < quiz.length;i++) {
            if(quizArr[i][1].equals("+")){
                if((Integer.parseInt(quizArr[i][0]) + Integer.parseInt(quizArr[i][2])) == Integer.parseInt(quizArr[i][4])) {
                    answer[i] = "O";
                } else {
                    answer[i] = "X";
                }
            } else {
                if((Integer.parseInt(quizArr[i][0]) - Integer.parseInt(quizArr[i][2])) == Integer.parseInt(quizArr[i][4])) {
                    answer[i] = "O";
                } else {
                    answer[i] = "X";
                }
            }
        }
        
        return answer;
    }
}