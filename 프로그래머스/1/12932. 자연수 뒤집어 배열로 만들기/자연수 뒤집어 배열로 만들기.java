class Solution {
    public int[] solution(long n) {
        String[] stringList = Long.toString(n).split(""); // n을 String 배열로 나눠준다.
        int[] answer = new int [stringList.length]; // 문자열 배열 길이 만큼 answer 배열을 만들어준다.
        
        for(int i = stringList.length-1; i >= 0 ; i--) { // 거꾸로 answer 배열에 넣어주고 리턴한다.
            answer[answer.length - i - 1] = Integer.parseInt(stringList[i]);
        } 
        
        return answer;
    }
}