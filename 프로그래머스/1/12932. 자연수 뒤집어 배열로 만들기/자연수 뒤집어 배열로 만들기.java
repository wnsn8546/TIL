class Solution {
    public int[] solution(long n) {
        String[] stringList = Long.toString(n).split("");
        int[] answer = new int [stringList.length];
        for(int i = stringList.length-1; i >= 0 ; i--) {
            answer[answer.length - i - 1] = Integer.parseInt(stringList[i]);
        } 
        
        return answer;
    }
}