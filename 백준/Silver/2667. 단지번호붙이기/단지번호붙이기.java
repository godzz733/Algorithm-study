
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
	static int n,cnt;
	static int[][] arr;
	static int[] apart = new int[25*25];
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		cnt = 0;
		int result =0;
		n = sc.nextInt();
		arr = new int[n][n];
		for (int i=0; i<n; i++) {
			String str = sc.next();
			for (int j=0; j<n; j++) {
				if (str.charAt(j)=='0') {
					arr[j][i] = 0;
				} else {
					arr[j][i] = 1;
				}
			}
		}
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (arr[j][i]==1) {
					arr[j][i] = 0;
					cnt+=1;
					dfs(i,j);
				}
			}
		}
		Arrays.sort(apart);
		for (int i=0; i<apart.length; i++) {
			if (apart[i]!=0) {
				sb.append(apart[i]).append('\n');
				result ++;
			}
		}
		System.out.println(result);
		System.out.println(sb);
	}
	static void dfs(int x, int y) {
		apart[cnt]+=1;
		for (int i=0; i<4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx<0 || nx>=n || ny<0 || ny>=n) {
				continue;
			}
			if (arr[ny][nx]==1) {
				arr[ny][nx] = 0;
				dfs(nx,ny);
			}
							
		}
	}
}
