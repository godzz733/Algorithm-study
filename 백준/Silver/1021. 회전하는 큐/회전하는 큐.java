import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;


public class Main{

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int result = 0;
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		LinkedList<Integer> q = new LinkedList<>();
		for (int i=1; i<n+1; i++ ) {
			q.add(i);
		}


		while (st1.hasMoreTokens()) {
			int a = Integer.parseInt(st1.nextToken());
			int idx = q.indexOf(a);
			int half = 0;
			idx += 1;
			if (q.size()%2==0) {
				half = (q.size()/2);
			} else {
				half = (q.size()/2)+1;
			}
			
			if (idx<=half) {
				for (int i=0; i<idx-1; i++) {
					int temp = q.pollFirst();
					q.add(temp);
					result++;
				}
				q.pollFirst();
				
			} else {
				for (int i=0; i<q.size()-idx+1; i++) {
					int temp = q.pollLast();
					q.addFirst(temp);
					result++;
				}
				q.pollFirst();
				
			}
			
		}
		System.out.println(result);
	}
}