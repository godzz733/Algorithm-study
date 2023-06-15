import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main{

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		StringBuilder sb = new StringBuilder();
		sb.append("<");
		Deque<Integer> q = new ArrayDeque<>();
		for (int i=1; i<n+1; i++) {
			q.add(i);
		}
		while (q.size() > 1) {
			for (int i=0; i<m-1; i++) {
				q.add(q.poll());
			}
			sb.append(q.poll()).append(", ");
		}
		sb.append(q.poll());
		sb.append(">");
		System.out.println(sb);
	}
}