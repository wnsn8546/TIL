class Solution {
    public int solution(String t, String p) {
        // 숫자로 이루어진 문자열 t, p 가 주어질때, t에서 p와 길이가 같은 부분 문자열 중에서,
        // 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution을 완성
        int answer = 0;
        String[] tTemp = t.split(""); // t를 String배열로 쪼개놓는다.
        
        for(int i = 0; i < tTemp.length - p.length()+1; i++) { // 이중 포문으로 p길이만큼 t문자열을 쪼개고,
            String strTemp = "";
            for(int j = i; j < i + p.length(); j++) {
                strTemp += tTemp[j];
            }
            
            if( Long.parseLong(strTemp) <= Long.parseLong(p) ) { // 작거나 같은 수가 나오면 answer를 +1 해준다.
               answer++; 
            }
        }
         
        
        return answer;
    }
}