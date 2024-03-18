// 종이 자르기
class Solution {
    public int solution(int M, int N) {
        int answer = (M - 1) + (( N - 1) * M);
        return answer;
    }
}