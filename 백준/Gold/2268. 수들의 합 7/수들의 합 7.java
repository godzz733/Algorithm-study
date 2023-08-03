import java.io.*;
import java.util.*;
class Main {
	static long [] tree;
	static int n;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int size = (int)Math.ceil(Math.log(n)/Math.log(2));
		tree = new long[1<<(size+1)];
		for (int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			if ( a== 1) {
				int b = Integer.parseInt(st.nextToken());
				Long c = Long.parseLong(st.nextToken());
				update(1,0,n-1,b-1,c);
			}
			else {
				int b = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				if (b > c) {
					int tem = b;
					b = c;
					c = tem;
				}
				sb.append(query(1,0,n-1,b-1,c-1)).append('\n');
				}
		}
		System.out.println(sb);
		
	}
	static void update(int node, int start, int end, int idx, long val) {
		if ( idx < start || idx > end) return;
		if (start == end) {tree[node] = val; return;}
		update(node<<1, start, (start+end)>>1, idx, val);
		update((node<<1)+1, ((start+end)>>1)+1,end,idx,val);
		tree[node] = tree[node<<1] + tree[(node<<1)+1];
	}
	static long query(int node, int start, int end, int left, int right) {
		if (start > right || end < left) return 0;
		if (start >= left && end <= right) return tree[node];
		long l = query(node<<1,start,(start+end)>>1, left,right);
		long r = query((node<<1)+1,((start+end)>>1)+1,end,left,right);
		return l+r;
	}
	

}
