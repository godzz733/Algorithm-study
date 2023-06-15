import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Deque;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class Main{
	
	static class pos {
		int m,v;
		public pos(int m, int v) {
			this.m = m;
			this.v = v;
		}
	}
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		long result = 0;
		ArrayList<pos> arr = new ArrayList<>();
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			arr.add(new pos(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
		}
		arr.sort(new Comparator<pos>() {
			@Override
			public int compare(pos o1, pos o2) {
				return o1.m - o2.m;
			}
		});
		ArrayList<Integer> bag = new ArrayList<>();
		for (int i=0; i<m; i++) {
			bag.add(Integer.parseInt(br.readLine()));
		}
		bag.sort(new Comparator<Integer>() {

			@Override
			public int compare(Integer o1, Integer o2) {
				return o1-o2;
			}
		});
		PriorityQueue<pos> jew = new PriorityQueue<>(new Comparator<pos>() {
			@Override
			public int compare(pos o1, pos o2) {
				return o2.v - o1.v;
			}
		});
		int idx = 0;
		for (int i=0; i<m; i++) {
			while (idx <n && bag.get(i) >= arr.get(idx).m) {
				jew.add(arr.get(idx));
				idx++;
			}
			if (!jew.isEmpty()) {
				result += jew.poll().v;
			}
		}
		System.out.println(result);
				
	}
}