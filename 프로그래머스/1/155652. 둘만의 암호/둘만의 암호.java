// 둘만의 암호
class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        String[] sTemp = s.split("");
        String[] alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
        for(int i = 0; i < sTemp.length; i++) {
            for(int j = 0; j < alphabet.length; j++) {
                if(alphabet[j].equals(sTemp[i])) {
                    if(skip.contains(alphabet[(j+index)%26])) {
                        for(int k = 1;;k++) {
                            if(!(skip.contains(alphabet[(j+index+k)%26]))) {
                                answer += alphabet[(j+index+k)%26];
                                break;
                            }
                            
                        }
                        
                    }else {
                        answer += alphabet[(j+index)%26];
                    }
                }
            }    
        }
        
        
        
        return answer;
    }
}