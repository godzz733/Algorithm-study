import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main{

	static boolean [] visited;
	static class pos {
		int x,cnt;
		public pos(int x, int cnt) {
			this.x = x;
			this.cnt = cnt;
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int f=sc.nextInt(), s = sc.nextInt(), g = sc.nextInt(), u = sc.nextInt(), d = sc.nextInt();
		sc.close();
		Queue<pos> q = new LinkedList<>();
		q.add(new pos(s,0));
		visited = new boolean[1000101];
		visited[s] = true;
		int key = 0;
		while (!q.isEmpty()) {
			pos cur = q.poll();
			int x = cur.x;
			int cnt = cur.cnt;
			if (x==g) {
				System.out.println(cnt);
				key++;
				break;
			}
			if (x+u<=f && !visited[x+u]) {
				q.add(new pos(x+u,cnt+1));
				visited[x+u] = true;
			}
			if (x-d>0 && !visited[x-d]) {
				q.add(new pos(x-d,cnt+1));
				visited[x-d] = true;
			}
			if (x+u == g) {
				System.out.println(cnt+1);
				key++ ;
				break;
			}
			if (x-d == g) {
				System.out.println(cnt+1);
				key++;
				break;
			}
			
		}
		if (key==0) {
			System.out.println("use the stairs");
		}
		
		
	}

}