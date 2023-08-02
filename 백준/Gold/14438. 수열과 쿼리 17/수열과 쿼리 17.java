import java.io.*;
import java.util.*;
class Main {
	static StringBuilder sb = new StringBuilder();
	static int [] tree, arr;
	static int n;
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		n = Integer.parseInt(br.readLine());
		tree = new int[1<<(int)Math.ceil(Math.log(n)/Math.log(2))+1];
		st = new StringTokenizer(br.readLine());
		arr = new int[n];
		for (int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int m = Integer.parseInt(br.readLine());
		init(1,0,n-1);
		for (int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			if (a == 1) update(1,0,n-1,b-1,c);
			else System.out.println(query(1,0,n-1,b-1,c-1));
		}
		
		
	}
	static void init(int node,int start, int end) {
		if (start == end) {
			tree[node] = arr[start];
		} else {
			init(node*2,start,(start+end)/2);
			init(node*2+1,(start+end)/2+1,end);
			tree[node] = Math.min(tree[node*2], tree[node*2+1]);
		}
	}
	static void update(int node, int start, int end, int index, int val) {
		if (index < start || index > end) return;
		if (start == end) {
			arr[index] = val;
			tree[node] = val;
			return;
		}
		update(node*2,start,(start+end)/2, index, val);
		update(node*2+1,(start+end)/2+1,end,index,val);
		tree[node] = Math.min(tree[node*2], tree[node*2+1]);
	}
	static int query(int node, int start, int end, int left, int right) {
		if (left > end || right < start) return -1;
		if (left <= start && right >= end) return tree[node];
		int l = query(node*2,start,(start+end)/2,left,right);
		int r = query(node*2+1,(start+end)/2+1,end,left,right);
		if (l == -1) return r;
		else if (r == -1) return l;
		else return Math.min(l,r);
	}
	

}
