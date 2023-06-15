import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main{
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String [] input = br.readLine().split(" ");
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(input[0]);
		int m = Integer.parseInt(input[1]);
		int [] indegrees = new int[n+1];
		ArrayList<ArrayList<Integer>> arr = new ArrayList<ArrayList<Integer>>();
		for (int i=0; i<n+1; i++) {
			arr.add(new ArrayList<Integer>());
		}
		for (int i=0; i<m; i++) {
			input = br.readLine().split(" ");
			arr.get(Integer.parseInt(input[0])).add(Integer.parseInt(input[1]));
			indegrees[Integer.parseInt(input[1])]++;
		}
		Queue<Integer> q = new LinkedList<>();
		for (int i=1; i<n+1; i++) {
			if (indegrees[i] == 0)  q.add(i);
		}
		
		while (!q.isEmpty()) {
			int a = q.poll();
			sb.append(a).append(" ");
			for (int num : arr.get(a)) {
				indegrees[num]--;
				if (indegrees[num]==0) q.add(num);
			}
		}
		br.close();
		System.out.println(sb);
	}
}