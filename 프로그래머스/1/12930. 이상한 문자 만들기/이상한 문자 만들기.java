class Solution {
    public String solution(String s) {
        // 문자열 s는 한 개 이상의 단어로 구성되어있다.
        // 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
        // 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴해라.
        // 띄어쓰기가 나오면 카운트 변수를 초기화 하면서 카운트 변수로 홀수인지 짝수인지 구분해서
        // 새로운 문자열로 바꿔서 리턴한다.
        String answer = "";
        String[] splitS = s.split(""); // 문자열 배열로 쪼개서 임시 변수에 넣는다.
        int count = 0; // 짝수번째인지 홀수번째 인지 판별하기 위한 카운트변수
        
        for(int i = 0; i < splitS.length; i++) {
            count++; // 문자마다 카운트변수를 +1;
            if(splitS[i].equals(" ")) {// 문자가 공백이면 count 변수를 0으로 초기화 하고 공백을 넣어준다.
                count = 0;
                answer += " ";
            } else if(count % 2 == 0){ // 짝수번째이면 알파벳을 소문자로 바꿔서 넣어준다.
                answer += splitS[i].toLowerCase();
            } if(count % 2 == 1){ // 홀수번째이면 알파벳을 대문자로 바꿔서 넣어준다.
                answer += splitS[i].toUpperCase();
            }
        }
        
        
        return answer;
    }
}