import java.io.*;
import java.util.*;
class Main {
	static long [] arr,tree;
	static int n;
	static int mod = 1000000007;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken());
		arr = new long[n+1];
		tree = new long[1<<((int)Math.ceil(Math.log(n)/Math.log(2))+1)];
		for (int i=0; i<n; i++) {
			arr[i] = Long.parseLong(br.readLine());
		}
		init(1,0,n-1);
		for (int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			if (a == 1) {
				Long c = Long.parseLong(st.nextToken());
				update(1,0,n-1,b-1,c);
			}
			else {
				int c = Integer.parseInt(st.nextToken());
				sb.append(query(1,0,n-1,b-1,c-1)).append('\n');
				}
		}
		System.out.println(sb);
		
		
	}
	static void init(int node, int start, int end) {
		if (start == end) tree[node] = arr[start];
		else {
			init(node<<1, start, (start+end)>>1);
			init((node<<1)+1,((start+end)>>1)+1,end);
			tree[node] = (tree[node<<1] % mod) * (tree[(node<<1)+1]%mod) % mod;
		}
	}
	static void update(int node, int start, int end, int idx, long val) {
		if (start > idx || end < idx) return;
		if (start == end) tree[node] = val;
		else {
			update(node<<1, start, (start+end)>>1, idx, val);
			update((node<<1)+1,((start+end)>>1)+1,end,idx,val);
			tree[node] = (tree[node<<1]%mod) * (tree[(node<<1)+1] % mod) % mod;
		}
	}
	static long query(int node, int start, int end, int left, int right) {
		if (start > right || end < left) return 1;
		if (start >= left && end <= right) return tree[node];
		long l = query(node<<1, start, (start+end)>>1, left,right);
		long r = query((node<<1)+1,((start+end)>>1)+1, end,left,right);
		return (l%mod) * (r%mod) % mod;
	}
	

}
