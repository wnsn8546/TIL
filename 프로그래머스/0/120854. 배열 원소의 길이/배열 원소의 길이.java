class Solution {
    public int[] solution(String[] strlist) {
        // 원소별로 길이를 담은 배열을 리턴하기
        int[] answer = new int[strlist.length];
        
        for(int i = 0; i < strlist.length;i++) {
            answer[i] = strlist[i].length();
        }
        
        return answer;
    }
}