import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main{
	static int num;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		PriorityQueue<Integer> min = new PriorityQueue<>();
		PriorityQueue<Integer> max = new PriorityQueue<>(Collections.reverseOrder());
		int min_size = 0, max_size = 0;
		int n = Integer.parseInt(br.readLine());
		for (int i=0; i<n; i++) {
			int a = Integer.parseInt(br.readLine());
			if (min_size==max_size) {
				max.add(a);
				max_size++;
			} else {
				min.add(a);
				min_size++;
			}
			if (min_size>0 && max_size>0) {
			if (min.peek()<max.peek()) {
				int tema = min.poll();
				int temb = max.poll();
				min.add(temb);
				max.add(tema);
			}
			}
			sb.append(max.peek()).append('\n');
		}
		System.out.println(sb);
	}

}