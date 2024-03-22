import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        
        String answer = "";
        
        for(int i = 0; i < a.length(); i++) {
            if(a.charAt(i) != ' ') answer += Character.toString(a.charAt(i));
        }
        for(int i = 0; i < b.length(); i++) {
            if(b.charAt(i) != ' ') answer += Character.toString(b.charAt(i));
        }
            
        System.out.println(answer);
    }
}