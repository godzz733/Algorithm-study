import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	
	static int m,n,k;
	static int[][] arr;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	
	static void dfs(int x, int y) {
		arr[x][y] = 0;
		for (int i = 0; i<4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx<0 || nx>=m || ny<0 || ny>=n) {
				continue;
			}
			if (arr[nx][ny]==1) {
				arr[nx][ny] = 0;
				dfs(nx,ny);
			
			}
		}
	}
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		for (int i=0; i<tc; i++) {
			int result = 0 ;
			m = sc.nextInt();
			n = sc.nextInt();
			k = sc.nextInt();
			arr = new int[m][n];
			for (int j=0; j<k; j++) {
				int a = sc.nextInt(), b = sc.nextInt();
				arr[a][b] = 1;
				
			}
			for (int q=0; q<m; q++) {
				for (int w=0; w<n; w++) {
					if (arr[q][w]==1) {
						dfs(q,w);
						result++;
					}
				}
			}
			System.out.println(result);
		}
		}
		
	}