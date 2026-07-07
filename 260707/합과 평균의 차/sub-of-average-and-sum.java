import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int total = a + b + c;
        int average = (a + b + c) / 3;
        int diff = total - average;

        System.out.println(total);
        System.out.println(average);
        System.out.println(diff);
    }
}