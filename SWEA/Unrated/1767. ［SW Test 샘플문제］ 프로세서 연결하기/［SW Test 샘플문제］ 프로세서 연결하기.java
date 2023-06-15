import java.io.*;
import java.util.*;

public class Solution{
	static int n, line, core;
	static StringBuilder sb = new StringBuilder();
	static int [][] arr;
	static List<int []> process;
	static final int [] dx = {1,-1,0,0}, dy = {0,0,1,-1};
	
	public static void main(String [] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int t = Integer.parseInt(br.readLine());
		for (int tc=1; tc<=t; tc++) {
			sb.append("#" + tc + " ");
			core = 0;
			line = 0;
			n = Integer.parseInt(br.readLine());
			process = new ArrayList<int[]>();
			arr = new int[n][n];
			for (int i=0; i<n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j=0; j<n; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
					if (i == 0 || i == n-1 || j == 0 || j == n-1) continue;
					if (arr[i][j] == 1) process.add(new int[] {i,j});
			}
			}
			dfs(0, 0, 0);
			sb.append(line + "\n");	
		}
		System.out.println(sb);
	}
	// x = 현재 볼 코어, cnt = 연결된 코어수, line = 연결한 전선 길이
	public static void dfs(int x, int cnt, int core_line) {
		if (cnt == core) {
			line = Math.min(line, core_line);
		} else if (cnt > core) {
			core = cnt;
			line = core_line;
		}
		if (x == process.size()) return;
		
		for (int i=0; i<4; i++) {
			int len = check(process.get(x),i);
			if (len == -1) continue;
			core_line += len;
			cnt++;
			dfs(x+1, cnt, core_line);
			rollback(process.get(x), i);
			cnt--;
			core_line -= len;
		}
		dfs(x+1, cnt, core_line);
	}
	// 이 프로세서를 연결할 수 있을지 확인 하고 연결할 수 있으면 연결함 + 전선길이 체크
	public static int check(int [] xy, int i){
		int cnt=0;
		int nx = xy[0] + dx[i], ny = xy[1] + dy[i];
		while (inrange(nx,ny)) {
			if (arr[nx][ny] != 0) return -1;
			nx += dx[i];
			ny += dy[i];
		}
		nx = xy[0] + dx[i];
		ny = xy[1] + dy[i];
		while (inrange(nx,ny)) {
			arr[nx][ny] = 2;
			nx += dx[i];
			ny += dy[i];
			cnt++;
		}
		return cnt;
	}
	// 전선 연결 끊기
	public static void rollback(int [] xy, int i) {
		int nx = xy[0] + dx[i], ny = xy[1] + dy[i];
		while (inrange(nx,ny)) {
			arr[nx][ny] = 0;
			nx += dx[i];
			ny += dy[i];
		}
	}
	// x,y가 범위안에 있는지 없는지 확인, 범위 안이면 true 밖이면 false 반환함
	public static boolean inrange(int x, int y) {
		return !(x<0 || x>=n || y<0 || y>=n);
	}
	

}