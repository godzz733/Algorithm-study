import java.io.*;
import java.util.*;


public class Main{

	static int [][] arr;
	static boolean [][] visited;
	static int [] dx = {1,-1,0,0};
	static int [] dy = {0,0,1,-1};
	static int n, m, k, cnt;
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken()); m = Integer.parseInt(st.nextToken()); k = Integer.parseInt(st.nextToken());
		int num = 0;
		ArrayList<Integer> result = new ArrayList<>();
		arr = new int [n][m];
		visited = new boolean [n][m];
		for (int i=0; i<k; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken()), d =Integer.parseInt(st.nextToken());
			for (int j=b; j<d; j++) {
				for (int k = a; k<c; k++) {
					arr[j][k] = 1;
				}
			}
		}
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				cnt = 0;
				num += dfs(i,j);
				if (cnt != 0) {
					result.add(cnt);
				}
			}
		}
		Collections.sort(result);
		System.out.println(num);
		for (int i=0; i<result.size(); i++) {
			System.out.print(result.get(i) + " ");
		}
	}
	public static int dfs(int x, int y) {
		if (x<0 || x>=n || y<0 || y>=m || visited[x][y] || arr[x][y] == 1) return 0; 
		visited[x][y] = true;
		cnt++;
		for (int i=0; i<4; i++) {
			dfs(x+dx[i], y+dy[i]);
		}
		return 1;
	}
	
}