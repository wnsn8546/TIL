import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        ArrayList<Integer> arrList = new ArrayList<>();
        ArrayList<Integer> deleteList = new ArrayList<>();
        
        for(int n : arr) {
            arrList.add(n);
        }
        for(int n : delete_list) {
            deleteList.add(n);
        }

        for(int i = 0; i < arr.length; i++) {
            if(deleteList.contains(arr[i])) {
                arrList.remove(Integer.valueOf(arr[i]));
            }
        }
        
        int[] answer = new int[arrList.size()];
        
        for(int i = 0; i < answer.length; i++) {
            answer[i] = arrList.get(i);
        }
        
        return answer;
    }
}