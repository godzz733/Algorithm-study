import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		while (true) {
		int a = sc.nextInt(), b = sc.nextInt();
		if (a==0 && b==0) {
			break;
		} else {
			
		if (a>b) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}
		}
		}
	}
}