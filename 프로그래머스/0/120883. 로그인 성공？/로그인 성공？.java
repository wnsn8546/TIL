class Solution {
    public String solution(String[] id_pw, String[][] db) {
        String answer = "";
        // 반복문과 if문을 사용해서 둘 다 일치할때, 아이디만 일치할때, 아이디가 일치하는 회원이 없을때로 나눠서 리턴한다.
        for(int i = 0; i < db.length; i ++) {
            if(id_pw[0].equals(db[i][0]) && id_pw[1].equals(db[i][1])) {
                answer = "login";
                return answer;
            } else if(id_pw[0].equals(db[i][0])) {
                answer = "wrong pw";
                return answer;
            }
        }
        answer = "fail";
        
        return answer;
    }
}