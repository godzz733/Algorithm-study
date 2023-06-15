import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;


public class Main{
	static int n, m;
	static int [][][] visited;
	static int [][] arr;
	static int [] dx = {1,-1,0,0};
	static int [] dy = {0,0,1,-1};
	static class pos{
		int x,y,cnt,wall;
		public pos(int x,int y, int cnt, int wall) {
			this.x = x;
			this.y = y;
			this.cnt = cnt;
			this.wall = wall;
		}
	}
	public static int bfs(int [][][] visited, int [][] arr) {
		Deque<pos> q = new ArrayDeque<Main.pos>();
		q.add(new pos(0,0,1,0));
		visited[0][0][0] = 1;
		while (!q.isEmpty()) {
			pos cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			int cnt = cur.cnt;
			int wall = cur.wall;
			for (int i=0; i<4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx == n-1 && ny == m-1) {
					return cnt + 1;
				}
				if (nx<0 || nx>=n || ny<0 || ny>=m) {
					continue;
				}
				if (arr[nx][ny] == 0) {
					if (visited[nx][ny][wall] == 0) {
						q.add(new pos(nx,ny,cnt+1,wall));
						visited[nx][ny][wall] = 1;
					}
				} else {
					if (wall == 0 && visited[nx][ny][1] == 0) {
						q.add(new pos(nx,ny,cnt+1,1));
						visited[nx][ny][1] = 1;
					}
				}
			}
			
		}
		return -1;
	}
	
	
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken()); m = Integer.parseInt(st.nextToken());
		visited = new int [n][m][2];
		arr = new int [n][m];
		for (int i=0; i<n; i++) {
			String [] input = br.readLine().split("");
			for (int j=0; j<m; j++) {
				arr[i][j] = Integer.parseInt(input[j]);
			}
		}
		if (n==1 && m == 1) {
			System.out.println("1");
		} else {
			System.out.println(bfs(visited,arr));
		}

		
	}
}