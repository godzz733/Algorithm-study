import java.util.Arrays;
import java.util.Scanner;

public class Main{
	
	static int n,m;
	static int[] arr;
	static int[] lst;
	static StringBuilder sb = new StringBuilder();
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		arr = new int[m];
		lst = new int[n];
		for (int i=0; i<n; i++) {
			lst[i] = sc.nextInt();
		}
		sc.close();
		Arrays.sort(lst);
		backtracking(0, 0);
		System.out.println(sb);
	}
	static void backtracking(int k, int depth) {
		if (depth==m) {
			for (int val:arr) {
				sb.append(val + " ");
			}
			sb.append('\n');
			return;
		}
		for (int i=k; i<n; i++) {
			arr[depth] = lst[i];
			backtracking(i, depth+1);
		}
	}
}