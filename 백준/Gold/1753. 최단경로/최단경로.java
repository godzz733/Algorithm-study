import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int v,e,start;
	static ArrayList<ArrayList<pos>> arr;
	static class pos{
		int idx,d;
		public pos(int idx, int d) {
			this.idx = idx;
			this.d = d;
		}
	}
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String [] input = br.readLine().split(" ");
		v = Integer.parseInt(input[0]);
		e = Integer.parseInt(input[1]);
		start = Integer.parseInt(br.readLine());
		arr = new ArrayList<>();
		for (int i=0; i<v+1; i++) {
			arr.add(new ArrayList<>());
		}
		for (int i=0; i<e; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			arr.get(a).add(new pos(b,c));
		}
		int [] dist = new int[v+1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		PriorityQueue<pos> q = new PriorityQueue<>((o1,o2) -> Integer.compare(o1.d, o2.d));
		q.offer(new pos(start,0));
		dist[start] = 0;
		while(!q.isEmpty()) {
			pos cur = q.poll();
			if (dist[cur.idx] < cur.d) {
				continue;
			}
			for (int i=0; i<arr.get(cur.idx).size(); i++) {
				pos ncur = arr.get(cur.idx).get(i);
				int cost = cur.d + ncur.d;
				if (cost < dist[ncur.idx]) {
					dist[ncur.idx] = cost;
					q.offer(new pos(ncur.idx,cost));
				}
			}
		}
		for (int i=1; i<v+1; i++) {
			if (dist[i]!=Integer.MAX_VALUE) {
				System.out.println(dist[i]);
			} else {
				System.out.println("INF");
			}
		}
		
		
		
	}
}