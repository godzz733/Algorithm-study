import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;


public class Main{

	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		ArrayList<ArrayList<Integer>> arr = new ArrayList<ArrayList<Integer>>();
		String [] input = br.readLine().split(" ");
		int n = Integer.parseInt(input[0]);
		int m = Integer.parseInt(input[1]);
		
		for (int i=0; i<n+1; i++) {
			arr.add(new ArrayList<Integer>());
		}
		for (int i=0; i<m; i++) {
			input = br.readLine().split(" ");
			arr.get(Integer.parseInt(input[0])).add(Integer.parseInt(input[1]));
			arr.get(Integer.parseInt(input[1])).add(Integer.parseInt(input[0]));
		}
		Deque<Integer> q = new LinkedList<>();
		int [] visited = new int[n+1];
		int result = 0;
		for (int i=1; i<n+1; i++) {
			if (visited[i]==0) {
				q.add(i);
				result ++;
				visited[i] = 1;
				while (!q.isEmpty()) {
					int x = q.poll();
					for (int num: arr.get(x)) {
						if (visited[num]==0) {
							visited[num] = 1;
							q.add(num);
						}
					}
				}
			}
		}
		System.out.println(result);

	}
}