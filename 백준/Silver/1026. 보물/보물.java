import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		int[] b = new int[n];
		int result = 0;
		for (int i =0 ; i<n; i++) {
			int temp = sc.nextInt();
			a[i] = temp;
		}
		for (int i =0 ; i<n; i++) {
			int temp = sc.nextInt();
			b[i] = temp;
		}

		Arrays.sort(a);
		Arrays.sort(b);
		for (int i =0 ; i<n; i++) {
			result += a[i]*b[n-i-1];
		
		}
		System.out.println(result);
}
}