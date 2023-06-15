import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int result = 0;
		String arr = sc.next();
		for (int i=0; i<n; i++) {
			result += arr.charAt(i)-'0';
		}
		System.out.println(result);
	}
}