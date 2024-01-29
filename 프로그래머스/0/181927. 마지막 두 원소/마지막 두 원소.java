class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length+1];
        int size = num_list.length;
        int temp = 0;
        
        if (num_list[size-1] > num_list[size-2]) {
            temp = num_list[size-1] - num_list[size-2];
        } else {
            temp = num_list[size-1] * 2;
        }
        
        for (int i = 0; i < size; i++) {
            answer[i] = num_list[i];
        }
        
        answer[size] = temp;
        
        return answer;
    }
}