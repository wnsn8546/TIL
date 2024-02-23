// n^2 배열 자르기
class Solution {
    public int[] solution(int n, long left, long right) {
        // 1. 2차배열 생성했던부분 없애기
        // 2. 1차배열 전체 생성했던 부분 없애기
        // 3. 2중 포문 없애기 -> while, i, j 변수로 해결
        // 4. for문 해당 부분만 하기
        // 5. long문제 해결?? 해결 안해도 되나... 해결
        int[] answer = new int[(int)(right - left) + 1];

        long count = left; // left부터 right까지
        int index = 0; // answer에 순서대로 넣어줄때 필요한 인덱스값
        int i = 0; // 2중 for문 줄이기 위해서 i, j 변수를 만들어서 while문에서 사용한다.
        int j = 0; //
        
        while(count < right + 1) {
            i = (int) (count / n);
            j = (int) (count % n);
            
            if(i < j) {
                answer[index++] = j + 1;
            } else {
                answer[index++] = i + 1;
            }
            count++;
        }
        
        return answer;
    }
}