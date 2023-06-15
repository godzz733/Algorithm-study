import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int result_2 = 0;
		int result_5 = 0;
		for (int i=1; i<a+1; i++) {
			int temp = i;
			while (temp%2==0) {
				temp /=2;
				result_2 ++;
			}
			while (temp%5==0) {
				temp /=5;
				result_5 ++;
			}
		}
		System.out.println(Math.min(result_2, result_5));
	}
}
