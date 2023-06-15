import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main{

	static int n,m,h;
	static int[][][] arr;
	static int[] dx = {1,-1,0,0,0,0};
	static int[] dy = {0,0,1,-1,0,0};
	static int[] dz = {0,0,0,0,1,-1};
	static boolean [][][] visited;
	static class pos{
		int x,y,z,cnt;
		public pos(int x, int y, int z , int cnt) {
			this.x = x;
			this.y = y;
			this.z = z;
			this.cnt =cnt;
		}
	}	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		h = sc.nextInt();
		arr = new int[n][m][h];
		visited = new boolean[n][m][h];
		Queue<pos> q = new LinkedList<>();
		int result = 0, check=0;
		for (int k=0; k<h; k++) {
			for (int i=0; i<m; i++) {
				for (int j=0; j<n; j++) {
					arr[j][i][k] = sc.nextInt();
					if (arr[j][i][k]==1) {
						q.add(new pos(j,i,k,0));
						visited[j][i][k] = true;
					}
				}
			}
		}

		while (!q.isEmpty()) {
			pos cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			int z = cur.z;
			int cnt = cur.cnt;
			if (cnt>result) {
				result = cnt;
			}
			for (int i=0; i<6; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				int nz = z + dz[i];
				if (nx<0 || nx>=n || ny<0 || ny>=m || nz<0 || nz>=h) {
					continue;
				}
				if (arr[nx][ny][nz]==0 && !visited[nx][ny][nz]) {
					arr[nx][ny][nz] = 1;
					q.add(new pos(nx,ny,nz,cnt+1));
					visited[nx][ny][nz]=true;
				}
				
			}
		}
		for (int k=0; k<h; k++) {
			for (int i=0; i<m; i++) {
				for (int j=0; j<n; j++) {
					if (arr[j][i][k]==0) {
						check++;
						break;
					}
				}
			}
		}
		if (check>0) {
			System.out.println(-1);
		} else {
			System.out.println(result);
		}
			
		}
		
	}
