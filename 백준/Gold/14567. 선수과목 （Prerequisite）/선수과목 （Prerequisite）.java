import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main{
	static class pos{
		int x,cnt;
		public pos(int x, int cnt) {
			this.x = x;
			this.cnt = cnt;
		}
	}
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String [] input = br.readLine().split(" ");
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(input[0]);
		int m = Integer.parseInt(input[1]);
		int [] indegrees = new int[n+1];
		ArrayList<ArrayList<Integer>> arr = new ArrayList<ArrayList<Integer>>();
		int [] result = new int[n+1];
		for (int i=0; i<n+1; i++) {
			arr.add(new ArrayList<Integer>());
		}
		for (int i=0; i<m; i++) {
			input = br.readLine().split(" ");
			arr.get(Integer.parseInt(input[0])).add(Integer.parseInt(input[1]));
			indegrees[Integer.parseInt(input[1])]++;;
		}
		Queue<pos> q = new LinkedList<>();
		for (int i=1; i<n+1; i++) {
			if (indegrees[i]==0) {
				q.add(new pos(i,1));
				result[i] = 1;
			}
		}
		while (!q.isEmpty()) {
			pos cur = q.poll();
			int x = cur.x;
			int cnt = cur.cnt;
			for (int num: arr.get(x)) {
				indegrees[num]--;
				if (indegrees[num]==0) {
					result[num] = cnt+1;
					q.add(new pos(num,cnt+1));
				}
			}
		}
		for (int i=1; i<n+1; i++) {
			sb.append(result[i]).append(" ");
		}
		br.close();
		System.out.println(sb);
	}
}