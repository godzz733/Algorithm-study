import java.util.Scanner;

public class Main{
	
	static int n;
	static boolean [][] visited;
	static int [][] arr;
	static int [] dx = {1,-1,0,0};
	static int [] dy = {0,0,1,-1};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		arr = new int[n][n];
		int max = 0;
		int result = 0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				arr[i][j] = sc.nextInt();
				if (max<arr[i][j]) {
					max = arr[i][j];
				}
			}
		}
		for (int k=0; k<max+1; k++) {
			visited = new boolean[n][n];
			int cnt = 0;
			for (int i=0; i<n; i++) {
				for (int j=0; j<n; j++) {
					if (arr[i][j]>k && !visited[i][j]) {
						cnt++;
						dfs(i,j,k);
					}
				}
			}
			if (cnt>result) {
				result = cnt;
			}
		}
		System.out.println(result);
		sc.close();
		
		
	}
	static void dfs(int x, int y, int water) {
		for (int i=0; i<4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx<0 || nx>=n || ny<0 || ny>=n) {
				continue;
			}
			if (arr[nx][ny]>water && !visited[nx][ny]) {
				visited[nx][ny] = true;
				dfs(nx,ny,water);
			}
		}
	}
}