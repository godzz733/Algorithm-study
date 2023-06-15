import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main{
	static ArrayList<Integer>[] arr;
	static boolean visited[];
	static int n,m,v,x;
	static Queue<Integer> q;
	static StringBuilder sb;
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		v = sc.nextInt();
		sb = new StringBuilder();
		q = new LinkedList<Integer>();
		q.add(v);
		arr = new ArrayList[n+1];
		for (int i=1; i<=n; i++) {
			arr[i] = new ArrayList<>();
		}
		for (int i=0; i<m; i++) {
			int a = sc.nextInt(), b = sc.nextInt();
			arr[a].add(b);
			arr[b].add(a);
		}
		for (int i=1; i<=n; i++) {
			Collections.sort(arr[i]);
		}
		visited = new boolean[n+1];
		visited[v] = true;
		sb.append(v + " ");
		dfs(v);
		sb.append('\n');
		visited = new boolean[n+1];
		visited[v] = true;
		sb.append(v + " ");
		bfs(v);
		System.out.println(sb);
	}
	static void bfs(int v) {
		while (!q.isEmpty()) {
			x = q.poll();
			for (int k:arr[x]) {
				if (!visited[k]) {
					q.add(k);
					sb.append(k + " ");
					visited[k] = true;
				}
			}
			
		}
	}
	static void dfs(int v) {
		for (int k:arr[v]) {
			if (!visited[k]) {
				visited[k] = true;
				sb.append(k + " ");
				dfs(k);
			}
		}
	}
}