import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main{
	static int a;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		int n = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
		for (int i=0; i<n; i++) {
			a = Integer.parseInt(br.readLine());
			if (a == 0) {
				if (q.isEmpty()) {
					sb.append("0").append('\n');
				} else {
					sb.append(q.poll()).append('\n');
				}
			} else {
				q.add(a);
			}
		}
		System.out.println(sb);
	}

}