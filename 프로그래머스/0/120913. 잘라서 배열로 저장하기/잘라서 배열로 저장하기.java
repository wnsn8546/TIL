// 잘라서 배열로 저장하기
class Solution {
    public String[] solution(String my_str, int n) {
        String[] answer;
        if(my_str.length() % n != 0) { // answer 배열길이 정하기
            answer = new String[my_str.length() / n + 1];
        } else {
            answer = new String[my_str.length() / n];
        }

        String[] my_strArray = my_str.split(""); // 배열에 쪼개서 넣어주고
        
        for(int i = 0; i < answer.length; i++) { // 순회하면서 문자열을 넣어주고, 마지막 인덱스일때 break해준다.
            answer[i] = "";
            for(int j = i * n; j < i * n + n; j++) {
                if(j == my_str.length()) break;
                answer[i] += my_strArray[j];
            }
        }
        
        return answer;
    }
}