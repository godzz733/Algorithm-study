import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class Main{
	
	static int v,e;
	static int [] parent;
	
	static int find_parent(int x) {
		if (parent[x] != x) {
			parent[x] = find_parent(parent[x]);
		}
		return parent[x];
	}
	static void union_parent(int a, int b) {
		a = find_parent(a);
		b = find_parent(b);
		if (a<b) {
			parent[b] = a;
		} else {
			parent[a] = b;
		}
	}
	static class pos{
		int a,b,c;
		public pos(int a, int b, int c) {
			this.a = a;
			this.b = b;
			this.c = c;
		}
	}
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		v = Integer.parseInt(st.nextToken());
		e = Integer.parseInt(st.nextToken());
		double result = 0;
		parent = new int [v+1];
		PriorityQueue<pos> q = new PriorityQueue<>(new Comparator<pos>() {
			@Override
			public int compare(pos o1, pos o2) {
				return o1.c-o2.c;
			}
		});
		for (int i=0; i<e; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());
			q.add(new pos(a,b,c));
		}
		for (int i=1; i<v+1; i++) {
			parent[i] = i;
		}
		while (!q.isEmpty()) {
			pos cur = q.poll();
			int a = cur.a;
			int b = cur.b;
			int c = cur.c;
			if (find_parent(a) != find_parent(b)) {
				union_parent(a,b);
				result += c;
			}
		}
		System.out.println((int) result);
	}
}