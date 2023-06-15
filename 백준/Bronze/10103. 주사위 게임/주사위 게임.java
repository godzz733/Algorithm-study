import java.io.IOException;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int result_a = 100, result_b = 100;
		for (int i=0; i<t; i++) {
			int a = sc.nextInt(), b = sc.nextInt();
			if (a==b) {
				continue;
			} else {
				if (a>b) {
					result_b -= a;
				} else {
					result_a -= b;
				}
			}
		}
		System.out.println(result_a);
		System.out.println(result_b);
	}
}