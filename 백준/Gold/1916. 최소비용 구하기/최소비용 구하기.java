import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class Main{
	
	static class pos{
		int x,d;
		public pos(int x, int d) {
			this.x = x;
			this.d = d;
		}
	}
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int v = Integer.parseInt(br.readLine());
		int e = Integer.parseInt(br.readLine());
		ArrayList<ArrayList<pos>> arr = new ArrayList<ArrayList<pos>>();
		for (int i=0; i<v+1; i++) {
			arr.add(new ArrayList<pos>());
		}
		for (int i=0; i<e; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			arr.get(a).add(new pos(b,c));
		}
		StringTokenizer st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());
		int [] dist = new int[v+1];
		int [] rout = new int[v+1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		PriorityQueue<pos> q = new PriorityQueue<>((o1,o2) -> Integer.compare(o1.d, o2.d));
		dist[start] = 0;
		rout[start] = 1;
		q.offer(new pos(start,0));
		while(!q.isEmpty()) {
			pos cur = q.poll();
			int x = cur.x;
			int d = cur.d;
			if (d>dist[x]) {
				continue;
			}
			for (pos num: arr.get(x)) {
				int cost = d + num.d;
				if (cost < dist[num.x]) {
					dist[num.x]= cost;
					rout[num.x] = x;
					q.offer(new pos(num.x,cost));
				}
			}
		}
		System.out.println(dist[end]);


	}
}