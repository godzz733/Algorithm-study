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
		int n = Integer.parseInt(br.readLine());

		boolean [] visited = new boolean [n+1];
		int [] result = new int[n+1];
		StringBuilder sb = new StringBuilder();
		for (int i=0; i<n+1; i++) {
			arr.add(new ArrayList<Integer>());
		}
		for (int i=0; i<n-1; i++) {
			String [] input = br.readLine().split(" ");
			arr.get(Integer.parseInt(input[0])).add(Integer.parseInt(input[1]));
			arr.get(Integer.parseInt(input[1])).add(Integer.parseInt(input[0]));
		}
		Deque<Integer> q = new LinkedList<>();
		q.add(1);
		visited[1] = true;
		while (!q.isEmpty()) {
			int x = q.poll();
			for (int num: arr.get(x)) {
				if (!visited[num]) {
					visited[num] = true;
					result[num] = x;
					q.add(num);
				}
			}
		}
		for (int i=2; i<n+1; i++) {
			sb.append(result[i]).append('\n');
		}
		System.out.println(sb);


	}
}