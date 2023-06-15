import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main{
	
	static class pos{
		int x,idx;
		public pos(int x, int idx) {
			this.x = x;
			this.idx = idx;
		}
	}
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		int [] arr = new int[10001];
		PriorityQueue<pos> q = new PriorityQueue<>(new Comparator<pos>(){
			@Override
			public int compare(pos o1, pos o2) {
				return o2.x - o1.x;
			}
		});
		int result = 0;
		for (int i=0; i<n; i++) {
			String [] input = br.readLine().split(" ");
			int a = Integer.parseInt(input[0]), b = Integer.parseInt(input[1]);
			q.add(new pos(a,b));
		}
		while (!q.isEmpty()) {
			pos cur = q.poll();
			int a = cur.x;
			int b = cur.idx;
			if (arr[b] == 0) {
				result += a;
				arr[b] = 1;
			} else {
				while(b>0 && arr[b]!=0) {
					b--;
				}
				if (b>0) {
					result += a;
					arr[b] = 1;
				}
			}
		}
		System.out.println(result);
	}

}