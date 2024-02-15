import java.util.*;

public class Main {
    public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    String s = sc.nextLine();
    String[] sList = s.split("");
    String answer = "";

        for(String c : sList) { // 하나씩 순회하면서
            char cTemp = c.charAt(0);
            if(Character.isUpperCase(cTemp)) { // 대문자 일때
                answer += Character.toString(Character.toLowerCase(cTemp));
            } else { // 소문자 일때
                answer += Character.toString(Character.toUpperCase(cTemp));
            }
        }
        System.out.println(answer);
    }
}