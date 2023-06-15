import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt(), d = sc.nextInt(), e = sc.nextInt();
		int result = 0;
		result += Math.pow(a,2);
		result += Math.pow(b,2);
		result += Math.pow(c,2);
		result += Math.pow(d,2);
		result += Math.pow(e,2);
		System.out.println(result%10);
	}
}