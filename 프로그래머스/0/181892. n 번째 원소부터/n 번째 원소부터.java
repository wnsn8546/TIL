class Solution {
    public int[] solution(int[] num_list, int n) {

        int length = num_list.length - n + 1;
        int[] answer = new int[length];
        int count = 0;
        
        for(int i = n-1; i < num_list.length; i++) {
            answer[count++] = num_list[i];
        }
        
        return answer;
    }
}