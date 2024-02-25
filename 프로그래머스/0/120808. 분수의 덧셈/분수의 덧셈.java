// 분수의 덧셈
class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        // 분자는 서로 곱해서 더하고, 분모는 서로 곱하고, gcd로 약분하고 리턴.
        int[] answer = new int[2];
        
        // 분자
        answer[0] = ((numer1 * denom2) + (denom1 * numer2));
        // 분모
        answer[1] = (denom1 * denom2);
        
        int gcdNum = gcd(answer[0], answer[1]);
        
        answer[0] = answer[0] / gcdNum;
        answer[1] = answer[1] / gcdNum;
        
        return answer;
    }
    public static int gcd(int a, int b) { // 유클리드호제법 큰 수를 작은 수로 나누면서 나머지가 0이 될때 작은 수가 gcd
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}