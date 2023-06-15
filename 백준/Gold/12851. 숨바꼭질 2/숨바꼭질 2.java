import java.io.*;
import java.util.*;



public class Main {
	

	static int result, end,fast;
	static int [] visited;
	static Deque<Integer> q;
	
	public static void subin(int x, int cnt) {
		if (x<0 || x>100000) return;
		if (x == end) {
			if (fast == Integer.MAX_VALUE) {
				fast = cnt;
				visited[x] = cnt;
				result++;
			} else if (cnt == fast) {
				result ++;
			}
		} else {
			if (visited[x] != 0 && visited[x] != cnt) return;
			q.add(x);
			visited[x] = cnt;
		}
	}
	public static void main(String [] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		end = Integer.parseInt(st.nextToken());
		fast = Integer.MAX_VALUE;
		visited = new int [100001];
		q = new ArrayDeque<>();
		result = 0;
		q.add(start);
		while(!q.isEmpty()) {
			int x = q.poll();
			subin(x+1, visited[x] + 1);
			subin(x-1, visited[x] + 1);
			subin(x*2, visited[x] + 1);
			
		}
		if (start == end) {
			System.out.println(0);
			System.out.println(1);
		} else {
			bw.write(fast + "\n");
			bw.write(result + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
		
	}
}