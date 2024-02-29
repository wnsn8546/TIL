// 옹알이 (1)
class Solution {
    public int solution(String[] babbling) {
        // "aya", "ye", "woo", "ma" 를 최대 한 번씩만 사용해 조합해서 이어 붙인 발음밖에 못한다.
        // 조카가 발음할 수 있는 단어의 개수를 리턴해라.
        // count가 1이넘어가는 옹알이가 있다면 멈추고, while이 정상종료 되면, answer를 ++해준다.
        int answer = 0;

        for(int i = 0; i < babbling.length; i++) {
            String[][] babblingCount= {{"aya", "0"}, {"ye", "0"}, {"woo", "0"}, {"ma", "0"}};
            String tempStr = babbling[i];
            boolean flag = false; // 정상종료되면 true 아니면 false;

            while(tempStr.length() != 0) {
                for(int j = 0; j < babblingCount.length;j++) {
                    String t = babblingCount[j][0];
                    int length = tempStr.length();
                    for(int k = 0; k < length-babblingCount[j].length+1; k++) {
                        if(tempStr.length() >= babblingCount[j][0].length()+k) {
                            String tt = tempStr.substring(k, k + babblingCount[j][0].length());
                            if (tempStr.substring(k, k + babblingCount[j][0].length()).equals(babblingCount[j][0]) && babblingCount[j][1].equals("0")) {
                                tempStr = tempStr.replace(babblingCount[j][0], "*");
                                babblingCount[j][1] = "1";
                                j = -1;
                                break;
                            }
                        }
                    } if(tempStr.length() == 0) break;
                }
                tempStr = tempStr.replace("*", "");
                if(tempStr.length() == 0) flag = true;
                break;
            }
            if (flag == true) answer++;
        }

        return answer;
    }
}