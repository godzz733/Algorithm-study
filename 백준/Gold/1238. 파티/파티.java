import java.io.*;
import java.util.*;


class pos{
	int x,dist;
	pos(int x, int dist){
		this.x = x;
		this.dist = dist;
	}
}
public class Main {

	static int n,m,end;
	static Reader in = new Reader();
	static ArrayList<ArrayList<pos>> lst;
	static int [][] arr;
	static PriorityQueue<pos> q;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		n = in.nextInt(); m = in.nextInt(); end = in.nextInt();
		lst = new ArrayList<>();
		for (int i=0; i<n+1; i++) {
			lst.add(new ArrayList<pos>());
		}
		for (int i=0; i<m; i++) {
			lst.get(in.nextInt()).add(new pos(in.nextInt(), in.nextInt()));
		}
		q = new PriorityQueue<>(new Comparator<pos>() {
			@Override
			public int compare(pos o1, pos o2) {
				return o1.dist-o2.dist;
			}
		});
		arr = new int [n+1][n+1];
		for (int i=0; i<n+1; i++) {
			Arrays.fill(arr[i], 987654321);
		}
		int result = 0;
		for (int i=1; i<n+1; i++) {
			dik(i);
		}
		for (int i=1; i<n+1; i++) {
			result = Math.max(arr[i][end] + arr[end][i], result);
		}
		bw.write(result + "\n");
		bw.flush();
		bw.close();
		br.close();
			
	}
	public static void dik(int dot) {
		arr[dot][dot] = 0;
		q.add(new pos(dot,0));
		while (!q.isEmpty()) {
			pos cur = q.poll();
			int x = cur.x;
			int dist = cur.dist;
			if (arr[dot][x] < dist) continue;
			for (int i=0; i<lst.get(x).size(); i++) {
				int cost = dist + lst.get(x).get(i).dist;
				if (arr[dot][lst.get(x).get(i).x] > cost) {
					arr[dot][lst.get(x).get(i).x] = cost;
					q.add(new pos(lst.get(x).get(i).x, cost));
				}
			}
		}
	}
	static class Reader {
		final int SIZE = 1 << 13;
		byte[] buffer = new byte[SIZE];
		int index, size;

		int nextInt() throws Exception {
			int n = 0;
			byte c;
			while ((c = read()) <= 32)
				;
			boolean neg = c == '-' ? true : false;
			if (neg)
				c = read();
			do
				n = (n << 3) + (n << 1) + (c & 15);
			while (isNumber(c = read()));
			if (neg)
				return -n;
			return n;
		}

		boolean isNumber(byte c) {
			return 47 < c && c < 58;
		}

		byte read() throws Exception {
			if (index == size) {
				size = System.in.read(buffer, index = 0, SIZE);
				if (size < 0)
					buffer[0] = -1;
			}
			return buffer[index++];
		}
	}
	

}