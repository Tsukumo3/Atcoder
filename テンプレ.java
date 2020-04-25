import java.util.Scanner;

import java.util.List;
import java.util.ArrayList;

public class Main{
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        System.out.print("Input > ");

        //一行全部
        //String input = scanner.nextLine();

        // スペース分割
        //String input1 = scanner.next();
        //String input2 = scanner.next();
        //System.out.println(input1 + " " + input2);

        // 数字入力
        //int x = scanner.nextInt();
        //System.out.println(x);

        /*リスト化
        List<Integer> aList = new ArrayList<>();
        for(int i = 0; i <3; i++){
            Integer input1 = scanner.nextInt();
            aList.add(input1);
        }
        System.out.println(aList);
        */
        scanner.close();
    }
}
