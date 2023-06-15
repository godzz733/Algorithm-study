import java.io.*;
import java.util.*;



public class Main{

	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int m = Integer.parseInt(st.nextToken());
		ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
		for (int i=0; i<n+1; i++) {
			arr.add(new ArrayList<>());
		}
		for (int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken());
			arr.get(a).add(b);
			arr.get(b).add(a);
		}
		boolean visited [] = new boolean [n+1];
		visited[1] = true;
		int result = 0;
		Deque<Integer> q = new ArrayDeque<Integer>();
		for (int i=0; i<arr.get(1).size(); i++) {
			q.add(arr.get(1).get(i));
			visited[arr.get(1).get(i)] = true;
			result++;
		}
		while (!q.isEmpty()) {
			int x = q.poll();
			for (int i=0; i<arr.get(x).size(); i++) {
				if (!visited[arr.get(x).get(i)]) {
					q.add(arr.get(x).get(i));
					visited[arr.get(x).get(i)] = true;
					result++;
				}
			}
		}
		System.out.println(result);

	}
}