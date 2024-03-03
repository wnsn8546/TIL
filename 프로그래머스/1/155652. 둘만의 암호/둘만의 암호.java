// 둘만의 암호
class Solution {
    public String solution(String s, String skip, int index) {
String answer = "";
        String[] sTemp = s.split(""); // s를 sTemp 문자열 배열로 분해해놓는다.
        String[] skipArr = skip.split(""); // skip도 분해해 놓는다.
        String alphabet = "abcdefghijklmnopqrstuvwxyz"; // 알파벳 전부를 담은 문자열
        
        for(int i = 0;i < skipArr.length; i++){ // skip에 있는 알파벳을 먼저 지운다.
            alphabet = alphabet.replace(skipArr[i], "");
        }
        
        String[] alphabetArr = alphabet.split(""); // 분해해서 Arr에 넣는다.

        for(int i = 0; i < sTemp.length; i++) { // sTemp를 순회하면서,
            for(int j = 0; j < alphabetArr.length; j++) { // 해당 알파벳의 위치를 먼저 찾고
                if(alphabetArr[j].equals(sTemp[i])) {
                    answer += alphabetArr[(j + index) % alphabetArr.length]; // index 만큼 뒤에 있는 알파벳을 answer에 넣는다.
                }
            }
        }

        return answer;
    }
}