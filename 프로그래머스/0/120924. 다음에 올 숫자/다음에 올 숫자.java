class Solution {
    public int solution(int[] common) {
        int answer = 0;
        boolean isArithmetic = true;
        boolean isGeometric = false;
        
        int difference = common[1] - common[0];
        for(int i = 1; i < common.length-1; i++) {
            if(common[i+1]-common[i] != difference) {
                isArithmetic = false;
                break;
            }
        }
        
        if (isArithmetic != true) {
            difference = common[1] / common[0];
            answer = common[common.length-1] * difference;
        } else {
            answer = common[common.length-1] + difference;
        }
        
        return answer;
    }
}