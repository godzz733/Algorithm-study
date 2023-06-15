
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static class pos{
		int x,cnt;
		public pos(int x, int cnt) {
			this.x = x;
			this.cnt = cnt;
		}
		
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int st = sc.nextInt(), fi = sc.nextInt();
		Queue<pos> q = new LinkedList<>();
		q.add(new pos(st,0));
		int result = 0;
		boolean [] visited = new boolean[100001];
		visited[st] = true;
		while (!q.isEmpty()) {
			pos cur = q.poll();
			int x = cur.x;
			int cnt = cur.cnt;
			if (x==fi) {
				result = cnt;
				break;
			}
			if (0<=x-1 && !visited[x-1]) {
				visited[x-1] = true;
				q.add(new pos(x-1,cnt+1));
			}
			if (x+1<100001 && !visited[x+1]) {
				visited[x+1] = true;
				q.add(new pos(x+1, cnt+1));
			}
			if (x*2<100001 && !visited[x*2]) {
				visited[x*2] = true;
				q.add(new pos(x*2,cnt+1));
			}
		}
		System.out.println(result);
	}
}
