// 숫자 문자열과 영단어
class Solution {
    public int solution(String s) {
        int answer = 0;
        // 문자열을 해당 인덱스에 넣은 배열을 만들어주고,
        String[] arr = {"zero","one","two","three","four","five","six","seven","eight","nine"};
        
        for(int i=0;i<arr.length;i++) { // 배열에 들어 있는 문자열이 나오면 해당 인덱스로 교체해준다.
        	if(s.contains(arr[i])) {
        		s = s.replace(arr[i], Integer.toString(i));
        	}
        }
        
        answer = Integer.parseInt(s);
        
        return answer;
    }
}