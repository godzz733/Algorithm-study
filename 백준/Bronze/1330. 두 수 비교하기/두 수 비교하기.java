import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt();
		if (a>b) {
			System.out.println(">");
		} else if (a<b) {
			System.out.println("<");
		} else {
			System.out.println("==");
		}
		
	}
}