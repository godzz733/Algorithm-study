
import java.util.Scanner;

public class Main {
	static int n,cnt;
	static int [][] arr1;
	static int [][] arr2;
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	
	static int dfs1(int x, int y, int cnt) {
		for (int i=0; i<4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx<0 || nx>=n || ny<0 || ny>=n) {
				continue;
			}
			if (arr1[ny][nx]==cnt) {
				arr1[ny][nx]=0;
				dfs1(nx,ny,cnt);
			}
		}
		return 1;
	}
	static int dfs2(int x, int y, int cnt) {
		for (int i=0; i<4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx<0 || nx>=n || ny<0 || ny>=n) {
				continue;
			}
			if (arr2[ny][nx]==cnt) {
				arr2[ny][nx]=0;
				dfs2(nx,ny,cnt);
			}
		}
		return 1;
	}
	

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		arr1 = new int[n][n];
		arr2 = new int[n][n];
		int result1 = 0, result2 = 0 ;
		for (int i = 0; i<n; i++) {
			String str = sc.next();
			for (int j=0; j<n; j++) {
				char a = str.charAt(j);
				if (a=='R') {
					arr1[j][i] = 1;
					arr2[j][i] = 1; 
				} else if (a=='B') {
					arr1[j][i] = 2;
					arr2[j][i] = 2; 
				} else {
					arr1[j][i] = 3;
					arr2[j][i] = 1; 
				}
			}
		}
		for (int i =0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (arr1[j][i]>0) {
					cnt = arr1[j][i];
					arr1[j][i] = 0;
					result1 += dfs1(i,j,cnt);
				}
				if (arr2[j][i]>0) {
					cnt = arr2[j][i];
					arr2[j][i] = 0;
					result2 += dfs2(i,j,cnt);
				}
			}
		}
		System.out.println(result1 + " " + result2);
	}
}
