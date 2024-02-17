class Solution {
    public int solution(int[] number) {
        // 학생들은 각자 정수 번호를 갖고 있다.
        // 학생 3명의 정수번호를 더했을때 0이되면 삼총사라고 한다.
        // 학생들 중 삼총사를 만들 수 있는 방법의 수를 return 해라
        // 3명을 뽑아 0이 될때마다 answer를 +1씩
        int answer = 0;
        
        for(int i = 0; i < number.length; i++) {
            for(int j = i + 1; j < number.length; j++) {
                for(int k = j + 1; k < number.length; k++) {
                    if(number[i] + number[j] + number[k] == 0) {
                        answer++;
                    }
                }
            }
        }
    
        return answer;
    }
}