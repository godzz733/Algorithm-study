import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int j=0; j<t; j++) {
			int result_a = 0, result_b = 0;
			for (int i=0; i<9; i++) {
				int a = sc.nextInt(), b = sc.nextInt();
				result_a += a;
				result_b += b;
				}
			
			if (result_a>result_b) {
				System.out.println("Yonsei");
			} else if (result_a<result_b) {
				System.out.println("Korea");
			} else {
				System.out.println("Draw");
			}
		}
	}
}