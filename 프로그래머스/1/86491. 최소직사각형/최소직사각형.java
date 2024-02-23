// 최소직사각형
class Solution {
    public int solution(int[][] sizes) {
        // 다양한 모양과 크기의 명함들을 모두 수납해야 한다.
        // 가로, 세로 길이를 한쪽으로 돌려서 필요한 가로길이의 최대치, 세로길이의 최대치를 구한다.
        int answer = 0;
        int temp = 0; // 더 긴 쪽을 가로길이로 바꿔 놓기위해 임시로 담아놓을 변수
        int widthMax = 0; // 돌려 놓은 후, 가로길이 중 최대값을 담을변수.
        int heightMax = 0; // 돌려 놓은 후, 세로길이 중 최대값을 담을변수.
        
        for(int i = 0; i < sizes.length; i++) { // sizes를 순회하면서 가로길이보다 세로길이가 크면 가로길이와 바꾼다.
            if(sizes[i][0] < sizes[i][1]) {
                temp = sizes[i][1];
                sizes[i][1] = sizes[i][0];
                sizes[i][0] = temp;
            }
            if(widthMax < sizes[i][0]) widthMax = sizes[i][0]; // 현재까지의 가로 최대값보다 큰 가로값이면 바꿔준다.
            if(heightMax < sizes[i][1]) heightMax = sizes[i][1]; // 현재까지의 세로 최대값보다 큰 세로값이면 바꿔준다.
        }
        answer = widthMax * heightMax;
        
        return answer;
    }
}