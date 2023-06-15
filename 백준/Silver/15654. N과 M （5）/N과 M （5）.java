import java.util.Arrays;
import java.util.Scanner;

public class Main{
	
	static int n,m;
	static int [] arr;
	static int [] lst;
	static boolean [] visited;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		arr = new int[m];
		lst = new int[n];
		visited = new boolean[n];
		for (int i=0; i<n; i++) {
			lst[i] = sc.nextInt();
		}
		Arrays.sort(lst);
		sc.close();
		backtracking(0);
		System.out.println(sb);
	}
	public static void backtracking(int depth) {
		if (depth==m) {
			for (int val:arr) {
				sb.append(val + " ");
			}
			sb.append('\n');
			return;
		}
		for (int i = 0; i<n; i++) {
			if (!visited[i]) {
				visited[i] = true;
				arr[depth] = lst[i];
				backtracking(depth+1);
				visited[i] = false;
			}

		}
	}
}