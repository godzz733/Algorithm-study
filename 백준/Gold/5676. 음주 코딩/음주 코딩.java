import java.io.*;
import java.util.*;
class Main {
	static int [] tree, arr;
	static int n;
	static Map<Integer,ArrayList<Integer>> map = new HashMap();
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		String input = "";
		while ((input = br.readLine()) != null) {
			st = new StringTokenizer(input);
			n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			int size = (int)Math.ceil(Math.log(n)/Math.log(2));
			tree = new int[1<<size+1];
			arr = new int[n];
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<n; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			init(1,0,n-1);
			StringBuilder sb = new StringBuilder();
			for (int i=0; i<m; i++) {
				st = new StringTokenizer(br.readLine());
				String com = st.nextToken();
				if (com.equals("C")) {
					int x = Integer.parseInt(st.nextToken());
					int y = Integer.parseInt(st.nextToken());
					update(1,0,n-1,x-1,y < 0 ? -1 : (y > 0 ? 1 : 0));
				} else {
					int x = Integer.parseInt(st.nextToken());
					int y = Integer.parseInt(st.nextToken());
					int ans = query(1,0,n-1,x-1,y-1);
					if (ans < 0) sb.append("-");
					else if (ans > 0) sb.append("+");
					else sb.append("0");
				}
			}
			System.out.println(sb);
			}
		
	}
	static void init (int node, int start, int end) {
		if (start == end) {
			if (arr[start] <0) tree[node] = -1;
			else if (arr[start] > 0) tree[node] = 1;
			else tree[node] = 0;
		} else {
		init(node*2,start,(start+end)>>1);
		init(node*2+1,((start+end)>>1)+1,end);
		tree[node] = tree[node<<1] * tree[(node<<1)+1];
		}
	}
	static void update(int node, int start, int end, int idx, int val) {
		if (idx > end || idx < start) return;
		if (start == end) {
			arr[idx] = val;
			tree[node] = val;
			return;
		}
		update(node<<1,start,(start+end)>>1,idx,val);
		update((node<<1)+1,((start+end)>>1)+1,end,idx,val);
		tree[node] = tree[node<<1] * tree[(node<<1)+1];
	}
	static int query(int node, int start, int end, int left, int right) {
		if (start > right || end < left) return -2;
		if (start >= left && end <= right) return tree[node];
		int l = query(node<<1, start, (start+end)>>1,left,right);
		int r = query((node<<1)+1,((start+end)>>1)+1,end,left,right);
		if (l == -2) return r;
		if (r == -2) return l;
		if (l == 0 || r == 0) return 0;
		else return l*r;
	}
	

}
