import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		sc.close();
		for (int i=1; i<a+1; i++) {
			for (int j=0; j<i; j++) {
				System.out.print("*");
			}
			System.out.println("");
		}
		
		
	}
}