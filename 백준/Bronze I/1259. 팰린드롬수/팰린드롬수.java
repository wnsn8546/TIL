import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        while(true) {

            String s = sc.nextLine();

            if(s.equals("0")) break;

            String[] split = s.split("");
            String right = "";
            String reverse = "";

            for(int i = 0; i < split.length; i++) {
                right += split[i];
            }
            for(int i = split.length-1; i >= 0; i--) {
                reverse += split[i];
            }
            if(right.equals(reverse)) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }

        }
    }
}