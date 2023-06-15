import java.io.*;
import java.util.*;


public class Main{

	static int [][] arr;
	static boolean [][] visited;
	static int [] dx = {1,-1,0,0,1,1,-1,-1};
	static int [] dy = {0,0,1,-1,1,-1,1,-1};
	static int result, n, m;
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		while (true) {
			st = new StringTokenizer(br.readLine());
			m = Integer.parseInt(st.nextToken()); n = Integer.parseInt(st.nextToken());
			if (n == 0) break;
			arr = new int [n][m];
			visited = new boolean [n][m];
			result = 0;
			for (int i = 0; i<n; i++ ) {
				st = new StringTokenizer(br.readLine());
				for (int j=0; j<m; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			for (int i = 0; i<n; i++ ) {
				for (int j=0; j<m; j++) {
					result += dfs(i,j);
				}
			}
			System.out.println(result);
		}
	}
	public static int dfs(int x, int y) {
		if (x<0 || x>=n || y<0 || y>=m || visited[x][y] || arr[x][y] == 0) return 0; 
		visited[x][y] = true;
		arr[x][y] = 0;
		for (int i=0; i<8; i++) {
			dfs(x+dx[i], y+dy[i]);
		}
		return 1;
	}
	
}