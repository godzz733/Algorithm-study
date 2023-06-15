import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main{
	
	static class pos{
		int a,b;
		public pos(int a, int b) {
			this.a = a;
			this.b = b;
		}
	}
	static int x;
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		PriorityQueue<pos> q = new PriorityQueue<>(new Comparator<pos>() {
			@Override
			public int compare(pos o1, pos o2) {
				if (o1.a == o2.a) {
					return o1.b - o2.b;
				}
				return o1.a - o2.a;
			}
		});
		for (int i=0; i<n; i++) {
			x = Integer.parseInt(br.readLine());
			if (x != 0) {
				q.add(new pos(Math.abs(x),x));
			} else {
				if (q.size() == 0) {
					sb.append(0).append('\n');
				} else {
					sb.append(q.poll().b).append('\n');
				}
			}
		}
		System.out.println(sb);
	}
}