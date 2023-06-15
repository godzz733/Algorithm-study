import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i=0; i<t; i++) {
			int a = sc.nextInt(), b = sc.nextInt();
			int d = gcd(a,b);
			System.out.println((a*b)/d);
		}
		sc.close();
		
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