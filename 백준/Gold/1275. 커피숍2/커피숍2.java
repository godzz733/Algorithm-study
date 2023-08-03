import java.io.*;
import java.util.*;
class Main {
	static StringBuilder sb = new StringBuilder();
	static int n,m;
	static long [] tree, arr;
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		tree = new long [1 << ((int)Math.ceil(Math.log(n)/Math.log(2)) + 1)];
		arr = new long[n];
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<n; i++) {
			arr[i] = Long.parseLong(st.nextToken());
		}
		init(arr,tree,1,0,n-1);
		for (int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			Long d = Long.parseLong(st.nextToken());
			if (a > b) {
				int tem = a;
				a = b;
				b = tem;
			}
			sb.append(query(tree,1,0,n-1,a-1,b-1)).append('\n');
			update(arr,tree,1,0,n-1,c-1,d);
		}
		System.out.println(sb);
		
	}
	static void init(long[] a, long [] tree, int node, int start, int end) {
		if (start == end) {
			tree[node] = a[start];
		} else {
			init(a,tree,node*2,start,(start+end)/2);
			init(a,tree,node*2+1,(start+end)/2+1,end);
			tree[node] = tree[node*2] + tree[node*2+1];
		}
	}
	static void update(long[] a, long[] tree, int node, int start, int end, int index, long val) {
		if (index < start || index > end) return;
		if (start == end) {
			a[index] = val;
			tree[node] = val;
			return;
		}
		update(a,tree,node*2, start,(start+end)/2,index,val);
		update(a,tree,node*2+1,(start+end)/2+1,end,index,val);
		tree[node] = tree[node*2] + tree[node*2+1];
	}
	
	static long query(long[] tree, int node, int start, int end, int left, int right) {
		if (left > end || right < start) return 0;
		if (left <= start && right >= end) return tree[node];
		long left_sum = query(tree,node*2, start, (start+end)/2, left,right);
		long right_sum = query(tree,node*2+1,(start+end)/2+1, end,left,right);
		return left_sum + right_sum;
	}
	
	

}