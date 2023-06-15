import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a = sc.next(), b = sc.next();
		sc.close();
		int result_a = 0, result_b = 0;
		for (int i=0; i<3; i++) {
			result_a += Math.pow(10, i)*(a.charAt(i)-'0');
		}
		for (int i=0; i<3; i++) {
			result_b += Math.pow(10, i)*(b.charAt(i)-'0');
		}
		if (result_a<result_b) {
			System.out.println(result_b);
		} else {
			System.out.println(result_a);
		}
	}
}