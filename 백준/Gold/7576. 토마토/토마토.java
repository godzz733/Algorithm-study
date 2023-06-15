import java.io.*;
import java.util.*;

class pos{
	int x,y,cnt;
	pos (int x, int y, int cnt){
		this.x = x;
		this.y = y;
		this.cnt = cnt;
	}
}

public class Main{

	
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int m = Integer.parseInt(st.nextToken()), n = Integer.parseInt(st.nextToken());
		int [][] arr = new int [n][m];
		Deque<pos> q = new ArrayDeque<pos>();
		int [] dx = {1,-1,0,0};
		int [] dy = {0,0,-1,1};
		int result = 0;
		boolean [][] visited = new boolean [n][m];
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] == 1) {
					q.add(new pos(i,j,0));
					visited[i][j] = true;
				}
			}
		}
		while (!q.isEmpty()) {
			pos cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			int cnt = cur.cnt;
			result= Math.max(result, cnt);
			for (int i=0; i<4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx <0 || nx>=n || ny<0 || ny>=m || visited[nx][ny] || arr[nx][ny] == -1) continue;
				q.add(new pos(nx,ny,cnt+1));
				visited[nx][ny] = true;
				arr[nx][ny] = 1;
			}
		}
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				if (arr[i][j] == 0) {
					result = -1;
				}
			}
		}
		System.out.println(result);

	}
}