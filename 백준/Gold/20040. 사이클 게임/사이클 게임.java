import java.io.*;
import java.util.*;


public class Main {
	
	static int [] parent;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int result = 0;
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		parent = new int [n];
		for (int i=0; i<n; i++) {
			parent[i] = i;
		}
		for (int i=0; i<m; i++) {
			if (result != 0) {
				break;
			}
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken()), y = Integer.parseInt(st.nextToken());
			if (find(x) == find(y)) {
				result = i+1;
			} else {
				union(x,y);
			}
		}
		bw.write(result + "\n");
		bw.flush();
		bw.close();
		br.close();
			
	}
	public static int find(int x) {
		if (parent[x] != x) {
			parent[x] = find(parent[x]);
		}
		return parent[x];
	}
	public static void union(int a, int b) {
		a = find(a);
		b = find(b);
		if (a<b) {
			parent[b] = a;
		} else {
			parent[a] = b;
		}
	}
}