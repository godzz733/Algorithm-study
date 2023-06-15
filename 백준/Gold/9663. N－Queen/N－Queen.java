import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main{
	
	static int n;
	static int [] arr;
	static int result;
	static boolean can(int x) {
		for (int i=0; i<x; i++) {
			if (arr[i]==arr[x] || Math.abs(arr[i]-arr[x]) == Math.abs(i-x)) {
				return false;
			}
		}
		return true;
	}
	static void queen(int x) {
		if (x==n) {
			result++;
			return;
		}
		for (int i=0; i<n; i++) {
			arr[x] = i;
			if (can(x)==true) {
				queen(x+1);
			}
		}
		
	}
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		arr = new int[n];
		result = 0;
		queen(0);
		System.out.println(result);
	
	}
	
}