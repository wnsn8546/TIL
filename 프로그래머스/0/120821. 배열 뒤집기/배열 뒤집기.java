class Solution {
    public int[] solution(int[] num_list) {
        // 원소를 거꾸로 출력하기
        int[] answer = new int[num_list.length];
        
        for(int i = num_list.length-1; i >= 0; i--) {
            answer[num_list.length-i-1] = num_list[i];
        }
        
        return answer;
    }
}