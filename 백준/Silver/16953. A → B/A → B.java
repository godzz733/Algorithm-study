import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main{

	static class pos{
		long x,cnt;
		public pos(long x, long cnt) {
			this.x = x;
			this.cnt = cnt;
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long n = sc.nextInt();
		long m = sc.nextInt();
		int key = 0;
		sc.close();
		HashSet<Integer> visited = new HashSet<>();
		Queue<pos> q = new LinkedList<>();
		q.add(new pos(n,0));
		while (!q.isEmpty()) {
			pos cur = q.poll();
			long x = cur.x;
			long cnt = cur.cnt;
			if (x*2<m) {
				q.add(new pos(x*2,cnt+1));
			} 
			if (x*10+1<m) {
				q.add(new pos(x*10+1, cnt+1));
			} 
			if (x*2==m) {
				System.out.println(cnt+2);
				key++;
				break;
			} 
			if (x*10+1==m) {
				System.out.println(cnt+2);
				key++;
				break;
			}
		}
		if (key==0) {
			System.out.println(-1);
		}
	}

}