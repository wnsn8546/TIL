import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 단어 S와 정수 i가 주어졌을 때, S의 i번째 글자를 출력하는 프로그램.

        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();
        String[] sList = s.split("");
        int i = sc.nextInt();
        
        for(int j = 0; j < sList.length ; j++) {
            if(j == i-1) {
                System.out.println(sList[j]);
                break;
            }
        }

    }
}