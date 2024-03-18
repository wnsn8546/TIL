import java.util.*;
// 소수 만들기
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int sum = 0;
        
        for(int i = 0; i < nums.length - 2; i++) { // 모든 조합 소수인지 판별하기
            for(int j = i + 1; j < nums.length - 1; j++) {
                for(int k = j + 1; k < nums.length; k++) {
                    sum = nums[i] + nums[j] + nums[k];
                    if(isPrimeNumber(sum)) answer++;
                }
            }
        }
        
        return answer;
    }
    
    private static boolean isPrimeNumber(int sum) { // 소수 판별
        boolean isPrime = true;

        for(int i = 2; i <= sum / 2; i++) {
            if(sum % i == 0) {
                isPrime = false;
                break;
            }
        }

        return isPrime;
    }
}
