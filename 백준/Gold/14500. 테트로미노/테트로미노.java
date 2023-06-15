import java.util.Scanner;

public class Main{
	static int n,m,so,cnt,result;
	static int [][] arr;
	static int [] dx = {1,-1,0,0};
	static int [] dy = {0,0,1,-1};
	static boolean [][] visited;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		cnt = 0;
		result = 0;
		visited = new boolean[m][n];
		arr = new int[m][n];
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				arr[j][i] = sc.nextInt();
			}
		}
		sc.close();
		so = 0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				visited[j][i] = true;
				dfs(j,i,1,arr[j][i]);
				visited[j][i] = false;
			}
		}
		System.out.println(so);

	}
	static void dfs(int x, int y, int cnt, int result) {
		if (cnt==4) {
			if (result>so) {
				so = result;
			}
			return;
		}
		for (int i=0; i<4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx<0 || nx>=m || ny<0 || ny>=n) {
				continue;
			}
			if (!visited[nx][ny]) {
				if (cnt==2) {
					visited[nx][ny] = true;
					dfs(x,y,cnt+1,result+arr[nx][ny]);
					visited[nx][ny] = false;
				}
				visited[nx][ny] = true;
				dfs(nx,ny,cnt+1,result+arr[nx][ny]);
				visited[nx][ny] = false;
			}
		}
	}
	
}
