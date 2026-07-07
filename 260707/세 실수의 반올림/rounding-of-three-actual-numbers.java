import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.

        Scanner sc = new Scanner(System.in);

        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();

        System.out.println(String.format("%.3f", a));
        System.out.println(String.format("%.3f", b));
        System.out.println(String.format("%.3f", c));
    }
}