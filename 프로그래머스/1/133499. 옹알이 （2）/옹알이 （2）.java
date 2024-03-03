// 옹알이 (2)
class Solution {
    public int solution(String[] babbling) {
        // "aya", "ye", "woo", "ma" 를 최대 한 번씩만 사용해 조합해서 이어 붙인 발음밖에 못한다.
        // 조카가 발음할 수 있는 단어의 개수를 리턴해라.
        // count가 1이넘어가는 옹알이가 있다면 멈추고, while이 정상종료 되면, answer를 ++해준다.
        int answer = 0;

        for(int i = 0; i < babbling.length; i++) { // babbling 배열을 순회하면서,
            String[] babblingCount= {"aya", "ye", "woo", "ma"}; // 카운트할 배열변수.
            String tempStr = babbling[i]; // 문자열을 변환시키면서 사용할 임시 문자열변수

            for(int j = 0; j < babblingCount.length;j++) { // 카운트할 배열을 순회하면서
                int length = tempStr.length(); // 매번length() 보다 시간효율이 훨씬 좋아서 쓸 length변수

                for(int k = 0; k <= length - babblingCount[j].length(); k++) { // 현재tempStr에서 카운트할 문자열이 있는지 순회한다.
                    if (tempStr.substring(k, k + babblingCount[j].length()).equals(babblingCount[j]) && !tempStr.contains(babblingCount[j]+babblingCount[j])) { // 옹알이 단어가 존재하고, 연속으로 존재하지 않으면,
                        tempStr = tempStr.replaceFirst(babblingCount[j], "*"); // 해당문자열을 "*"로 바꿔주고,
                        j = -1; // for문의 j를 초기화 해주고 break한 뒤, 반복한다.
                        break;
                    }
                }
            }
            tempStr = tempStr.replace("*", ""); // 다 끝나고, 존재하는 "*"을 빈 문자열로 바꿨을때,
            if(tempStr.length() == 0) answer++; // 길이가 0이면 완전히 발음가능한 옹알이 단어이기 떄문에 answer를 ++한다.
        }

        return answer;
    }
}