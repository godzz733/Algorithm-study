import java.io.*;
import java.util.*;

class pos{
	int x,y;
	pos (int x, int y){
		this.x = x;
		this.y = y;
	}
}

class Edge implements Comparable<Edge>{
	int start,end,weight;
	Edge(int start, int end, int weight){
		this.start = start;
		this.end = end;
		this.weight = weight;
	}
	@Override
	public int compareTo(Edge o) {
		return weight - o.weight;
	}
}
public class Main{

	static int [][] arr;
	static int n,m,cnt;
	static boolean [][] visited;
	static int [] dx = {1,-1,0,0};
	static int [] dy = {0,0,1,-1};
	static int [] dnx = {1,0,-1,0};
	static int [] dny = {0,1,0,-1};
	static Deque<pos> q;
	static ArrayList<Edge> lst;
	static int [] parent;
	public static void make_land(int x, int y){
		if (visited[x][y]) {
			return;
		}
		visited[x][y] = true;
		if (arr[x][y] == 0) return;
		cnt++;
		q.add(new pos(x,y));
		if (arr[x][y] != 0) arr[x][y] = cnt;
		while (!q.isEmpty()) {
			pos cur = q.poll();
			for (int i=0; i<4; i++) {
				int nx = cur.x + dx[i];
				int ny = cur.y + dy[i];
				if (nx<0 || nx>=n || ny<0 || ny>=m || visited[nx][ny]) {
					continue;
				}
				if (arr[nx][ny] != 0) {
					arr[nx][ny] = cnt;
					visited[nx][ny] = true;
					q.add(new pos(nx,ny));
				}
			}
		}
		
	}
	
	public static void link_land(int x, int y, int num) {
		for (int i=0; i<4; i++) {
			int nx = x + dnx[i];
			int ny = y + dny[i];
			int go = 1;
			while (true) {
				if (nx<0 || nx>=n || ny<0 || ny>=m || arr[nx][ny] == num) {
					break;
				}
				if (arr[nx][ny] !=0 && go <= 2) {
					break;
				}
				if (arr[nx][ny] != 0) {
					lst.add(new Edge(num, arr[nx][ny], go-1));
					break;
				} else {
					nx += dnx[i];
					ny += dny[i];
					++go;
				}
			}
		}
		
	}
	
	public static int find(int x) {
		if (x != parent[x]) {
			parent[x] = find(parent[x]);
		}
		return parent[x];
	}
	public static void union(int a, int b) {
		a = find(a);
		b = find(b);
		if (a<b) {
			parent[b] = a;
		} else {
			parent[a] = b;
		}
	}
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int [n][m];
		visited = new boolean [n][m];
		q = new ArrayDeque<>();
		lst = new ArrayList<>();
		cnt = 0;	
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				make_land(i,j);
			}
		}
		parent = new int [cnt+1];
		for (int i=1; i<cnt+1; i++) {
			parent[i] = i;
		}
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				if (arr[i][j] != 0) {
					link_land(i,j,arr[i][j]);
				}
			}
		}
		Collections.sort(lst);
		int result = 0;
		int linked = 0;
		for (int i=0; i<lst.size(); i++) {
			Edge now = lst.get(i);
			if (find(now.start) != find(now.end)) {
				result += now.weight;
				union(now.start,now.end);
				linked++;
			}
			if (linked == cnt) {
				break;
			}
		}
		if (linked+1 < cnt) {
			bw.write(-1 + "\n");
		} else {
			bw.write(result + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
			

	}
}