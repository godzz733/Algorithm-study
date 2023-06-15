import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int [] dp0 = new int[41];
		int [] dp1 = new int[41];
		dp0[0] = 1;
		dp1[1] = 1;
		int tc = sc.nextInt();
		for (int t = 0; t<tc; t++) {
			int n = sc.nextInt();
			for (int i=2; i<41; i++) {
				dp0[i] = dp0[i-2] + dp0[i-1];
				dp1[i] = dp1[i-2] + dp1[i-1];
			}
			System.out.println(dp0[n] + " " + dp1[n]);
		}
	}
}