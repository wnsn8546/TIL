// 문자열 다루기 기본
class Solution {
    public boolean solution(String s) {
        return s.matches("[0-9]{4}|[0-9]{6}"); // 몇일 전에 프로그래머스 책 보고 외움. 숫자로만4개 또는 숫자로만 6개이냐? false,true.
    }
}