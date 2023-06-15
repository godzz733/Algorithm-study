import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int result = 0, idx = 0;
		for (int i = 0; i<9; i++) {
			int a = sc.nextInt();
			if (a>result) {
				result = a;
				idx = i;
			}
		}
		System.out.println(result);
		System.out.println(idx+1);
		
	}
}