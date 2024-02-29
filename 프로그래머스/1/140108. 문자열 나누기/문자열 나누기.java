// 문자열나누기
class Solution {
    public int solution(String s) {
        // 문자열 s를 규칙에 따라 여러 문자열로 분해하기
        // 첫 문자를 x, 왼쪽으로 읽어나가면서 x와 x가 아닌 다른 글자들이 나온 횟수를 카운트,
        // 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리한다.
        // 분리하고 남은 문자 부분에 대해 이 과정을 반복한다.
        // 남은 부분이 없다면 종료.
        // 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 지금까지 읽은 문자열을 분리하고 종료.
        // 분해한 문자열의 개수를 return하라.
        int answer = 0;
        
        String x = "" + s.charAt(0);
        int xCount = 0;
        int notXCount = 0;
        for(int i = 0 ; i < s.length(); i++) {
            String temp = "" + s.charAt(i);
            if (temp.equals(x)) {
                xCount++;
            } else {
                notXCount++;
            }
            if(xCount == notXCount) {
                answer++;
                if(i == s.length() - 1) break;
                x = "" + s.charAt(i + 1);
                xCount = 0;
                notXCount = 0;
            } else if(xCount != notXCount && i == s.length() - 1) {
                answer++;
            }
        }

        return answer;
    }
}