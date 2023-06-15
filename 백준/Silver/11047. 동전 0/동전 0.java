
import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt();
		int [] arr = new int[n];
		int result = 0;
		for (int i=0; i<n; i++) {
			int a = sc.nextInt();
			arr[i] = a;
		}
		for (int i=n-1; i>=0; i--) {
			result += m/arr[i];
			m %= arr[i];
		}
		System.out.println(result);
	}
}