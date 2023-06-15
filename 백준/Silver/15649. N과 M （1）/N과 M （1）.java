import java.util.Scanner;

public class Main{
	
	static int n,m;
	static int [] arr;
	static StringBuilder sb = new StringBuilder();
	static boolean[] visited;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		arr = new int[m];
		visited = new boolean[n];
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
		for (int i = 1; i<n+1; i++) {
			if (!visited[i-1]) {
				visited[i-1] = true;
				arr[depth] = i;
				backtracking(depth+1);
				visited[i-1] = false;
			}
		}
	}
}