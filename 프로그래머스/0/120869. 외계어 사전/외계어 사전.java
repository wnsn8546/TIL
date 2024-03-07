import java.util.*;

class Solution {
    public int solution(String[] spell, String[] dic) {
        int answer = 2;
        
        Arrays.sort(spell);
        
        String strSpell = Arrays.toString(spell);
        
        for(int i = 0; i < dic.length; i++) {
            String[] temp = dic[i].split("");
            Arrays.sort(temp);
            String strTemp = Arrays.toString(temp);
            
            if(strSpell.equals(strTemp)) {
                answer = 1;
                break;
            }
        }
        
        return answer;
    }
}