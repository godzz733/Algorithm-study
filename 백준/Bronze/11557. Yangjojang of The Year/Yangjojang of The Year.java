import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i=0; i<t; i++) {
			String uni = "";
			int result = 0;
			int n = sc.nextInt();
			for (int j=0; j<n; j++) {
				String a = sc.next();
				int b = sc.nextInt();
				if (result < b) {
					result = b;
					uni = a;
				}
			}
			System.out.println(uni);
		}
	}
}