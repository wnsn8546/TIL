class Solution {
    public int solution(int n, int m, int[] section) {
        // 페인트가 칠해진 길이가n미터인 벽
        // 구역을 나눠일부만 페인트를 새로 칠해서 예산을 아끼려한다.
        // n개의 구역으로 나누고 왼쪽부터 1~n번까지 번호를 붙였습니다
        // 롤러의 길이는 m미터, 롤러는 벽을 벗어나면 안된다. 구역의 일부만 포함되도록 칠하면 안된다.
        // section 숫자를 탐색하면서 최소 최댓값차이가 m까지일때, answer++;
        // 해주고 그 다음 section값 탐색 계속 반복하기
        int answer = 0;
        int min = 100001; // 최대숫자 +1
        int max = 0;
        int temp = 0;
        for(int i = 0;i < section.length ;i++) {
            if(section[i] < min) min = section[i];
            if(section[i] > max) max = section[i];
            if(max - min > m - 1) {
                answer++;
                min = section[i];
                max = section[i];
            }
        }
        
        if (max >= min) answer++;
        
        return answer;
    }
}