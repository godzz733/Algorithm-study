import java.io.*;
import java.util.*;

public class Solution{
	static int [][] arr;
	static int n, ans;
	static boolean [][] visited;
	static StringBuilder sb = new StringBuilder();
	static final int [] dx = {-1,-1,-1,0,1,1,1,0};
	static final int [] dy = {-1,0,1,1,1,0,-1,-1};
	static ArrayList<int []> zero;
	public static void main(String [] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int x = Integer.parseInt(br.readLine());
		for (int tc=1; tc<=x; tc++) {
			sb.append("#" + tc + " ");
			n = Integer.parseInt(br.readLine());
			arr = new int[n][n];
			ans = 0;
			visited = new boolean[n][n];
			zero = new ArrayList<>();
			for (int i=0; i<n; i++) {
				String str = br.readLine();
				for (int j=0; j<n; j++) {
					if (str.charAt(j) != '.') {
						arr[i][j] = -1;
						visited[i][j] = true;
					} else {
						arr[i][j] = 9;
					}
				}
			}
			for (int i=0; i<n; i++) {
				for (int j=0; j<n; j++) {
					checknum(i,j);
				}
			}
			for (int [] cur : zero) {
				bfs(cur[0], cur[1]);
			}
			for (int i=0; i<n; i++) {
				for (int j=0; j<n; j++) {
					if (!visited[i][j]) ans++;
				}
			}
			sb.append(ans + "\n");
		}
		System.out.println(sb);
	}
	public static void checknum(int x, int y) {
		if (arr[x][y] == -1) return;
		int cnt = 0;
		for (int i=0; i<8; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			if (nx<0 || nx>=n || ny<0 || ny>=n) continue;
			if (arr[nx][ny] == -1) cnt++;
		}
		arr[x][y] = cnt;
		if (cnt == 0) {
			zero.add(new int[] {x,y});
		}
	}
	public static void bfs(int x, int y) {
		if (visited[x][y]) return;
		ArrayDeque<int []> q = new ArrayDeque<>();
		q.add(new int[] {x,y});
		visited[x][y] = true;
		while(!q.isEmpty()) {
			int [] cur = q.poll();
			for (int i=0; i<8; i++) {
				int nx = cur[0] + dx[i];
				int ny = cur[1] + dy[i];
				if (nx<0 || nx>=n || ny<0 || ny>=n || visited[nx][ny]) continue;
				visited[nx][ny] = true;
				if (arr[nx][ny] == 0) q.add(new int[] {nx,ny});
			}
		}
		ans++;
	}

}