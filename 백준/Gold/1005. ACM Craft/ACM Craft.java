import java.io.*;
import java.util.*;
class pos{
	int to, time;
	pos(int to, int time){
		this.to = to;
		this.time = time;
	}
}

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int t = Integer.parseInt(br.readLine());
		for (int k=0; k<t; k++) {
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
			int [] time = new int [n+1];
			int [] indegree = new int [n+1];
			int [] dp = new int [n+1];
			ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
			for (int i=0; i<n+1; i++) {
				arr.add(new ArrayList<Integer>());
			}
			st = new StringTokenizer(br.readLine());
			for (int i=1; i<n+1; i++) {
				time[i] = Integer.parseInt(st.nextToken());
			}
			for (int i=0; i<m; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken());
				indegree[b]++;
				arr.get(a).add(b);
			}
			Deque<pos> q = new LinkedList<pos>();
			for (int i=1; i<n+1; i++) {
				if (indegree[i] == 0) q.add(new pos(i,time[i]));
			}
			int end = Integer.parseInt(br.readLine());
			while (!q.isEmpty()) {
				pos cur = q.poll();
				int x = cur.to;
				int cnt = cur.time;
				if (x == end) {
					System.out.println(cnt);
					break;
				}
				for (int tem: arr.get(x)) {
					indegree[tem]--;
					dp[tem] = Math.max(dp[tem], cnt + time[tem]);
					if (indegree[tem] == 0) q.add(new pos(tem,dp[tem]));
				}
			}
			
			
		}

		bw.flush();
		bw.close();
		br.close();


			
	}
	
}