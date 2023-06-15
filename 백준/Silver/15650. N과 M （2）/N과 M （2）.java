import java.io.IOException;
import java.util.Scanner;

public class Main {
	
	static int n,m;
	static int [] arr;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		arr = new int[m];
		back(1,0);
		System.out.println(sb);
	}
	static void back(int st, int depth) {
		if (depth == m) {
			for (int val : arr) {
				sb.append(val + " ");
			}
			sb.append('\n');
			return;
		}
		for (int i =st; i<n+1; i++) {
			arr[depth] = i;
			back(i+1,depth+1);
		}
	}
	
}