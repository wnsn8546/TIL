import java.util.*;
// 문자열 내 마음대로 정렬하기
class Solution {
    public String[] solution(String[] strings, int n) {
        // 문자열리스트와, 정수n이 주어졌을때 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순정렬
        // n번째 알파벳순으로 정렬을 하고, 중복이 있으면 사전 순으로 또 정렬을 해야한다.
        // n번째 알파벳을 붙여서 단어를 만들어서 answer에 넣고, 정렬을 하고,
        // n번째 알파벳을 잘라서 다시 넣자.
        String[] answer = new String[strings.length]; // answer 배열 크기 strings 배열 크기만큼.
        
        for (int i = 0; i < answer.length; i++) { // 크기만큼 순회하면서
            answer[i] = Character.toString(strings[i].charAt(n)) + strings[i]; // n번째 알파벳 + 단어를 합쳐서넣는다.
        }
        
        Arrays.sort(answer); // 정렬한다.
        
        for (int i = 0; i < answer.length; i++) { // 다시 순회하면서, n번째 알파벳을 자르고 다시 넣는다.
            answer[i] = answer[i].substring(1, answer[i].length());
        }
        return answer;
    }
}