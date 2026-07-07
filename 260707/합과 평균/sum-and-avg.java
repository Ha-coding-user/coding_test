import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        double A = sc.nextDouble();
        double B = sc.nextDouble();

        int total = (int)A + (int)B;
        double average = (A + B) / 2;

        System.out.println(String.format("%d %.1f", total, average));
    }
}