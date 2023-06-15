import java.io.IOException;
import java.util.Scanner;

public class Main {
	
	static int n,m;
	static int [][] arr;
	static int [] dx = {1,-1,0,0};
	static int [] dy = {0,0,1,-1};
	static boolean [][] visited;
	static void dfs(int x, int y) {
		visited[y][x] = true;
		for (int i=0; i<4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx<0 || nx>=n || ny<0 || ny>=m) {
				continue;
			}
			if (!visited[ny][nx]) {
				if (arr[ny][nx]==1) {
					arr[ny][nx] = arr[y][x] + 1;
					dfs(nx,ny);
				}
			} else {
				if (arr[ny][nx]>1 && arr[ny][nx]>arr[y][x]+1) {
					arr[ny][nx] = arr[y][x] +1;
					dfs(nx,ny);
				}
			}
		}
	}
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		arr = new int[m][n];
		visited = new boolean[m][n];
		for (int i=0; i<n; i++) {
			String lst = sc.next();
			for (int j=0; j<m; j++) {
				arr[j][i] = (lst.charAt(j)-'0');
			}
		}
		dfs(0,0);
		System.out.println(arr[m-1][n-1]);
	}
}