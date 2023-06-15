import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;

public class Main{

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		String [] input = br.readLine().split(" ");
		int n = Integer.parseInt(input[0]), m = Integer.parseInt(input[1]);
		ArrayList<Integer> [] arr = new ArrayList[n+1];
		int [] topo = new int[n+1];
		for (int i=0; i<n+1; i++) {
			arr[i] = new ArrayList<>();
		}
		for (int i=0; i<m; i++) {
			input = br.readLine().split(" ");
			arr[Integer.parseInt(input[0])].add(Integer.parseInt(input[1]));
			topo[Integer.parseInt(input[1])]++;
		}
		PriorityQueue<Integer> q = new PriorityQueue<>();
		for (int i=1; i<n+1; i++) {
			if (topo[i] == 0) {
				q.add(i);
			}
		}
		while (!q.isEmpty()) {
			int x = q.poll();
			sb.append(x).append(" ");
			for (Integer i : arr[x]) {
				topo[i]--;
				if (topo[i] == 0) {
					q.add(i);
				}
			}
		}
		System.out.println(sb);
		
	}

}