import java.util.Scanner;

public class Main{
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        // スペース分割
        Integer s = scanner.nextInt();
        Integer t = scanner.nextInt();

        System.out.println(t-s+1);
        scanner.close();
    }
}
