import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt();
		int result = gcd(a,b);
		sc.close();
		System.out.println(result);
		System.out.println(a*b/result);
	}
	public static int gcd(int a,int b) {
		while (b!=0) {
			int r = a%b;
			a = b;
			b = r;
		}
		return a;
	}
}