import java.io.*;
import java.util.*;

class pos{
	int x,cnt;
	pos(int x, int cnt){
		this.x = x;
		this.cnt = cnt;
	}
}

public class Main {
	

	static int result, end;
	static int [] visited;
	static Deque<pos> q;
	
	public static void subin(int x, int cnt) {
		if (x<0 || x>100000 || visited[x] <= cnt) return;
		if (x == end) {
			result = Math.min(result, cnt);
			visited[x] = cnt;
		} else {
			q.add(new pos(x,cnt));
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
		visited = new int [100001];
		Arrays.fill(visited, Integer.MAX_VALUE);
		q = new ArrayDeque<>();
		result = Integer.MAX_VALUE;
		q.add(new pos(start,0));
		while(!q.isEmpty()) {
			pos cur = q.poll();
			subin(cur.x*2, cur.cnt);
			subin(cur.x+1, cur.cnt+1);
			subin(cur.x-1, cur.cnt+1);
			
		}
		if (start == end) {
			System.out.println(0);
		} else {
			bw.write(result + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
		
	}
}