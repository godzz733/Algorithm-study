import java.io.*;
import java.util.*;

public class Solution{
	static int ans,V,E,A,B;
	static Node[] arr;
	static ArrayList<Integer> ancestorA, ancestorB;
	static StringBuilder sb = new StringBuilder();
	static public class Node{
		List<Integer> children;
		int parents;
		Node(){
			this.children = new ArrayList<>();
			this.parents = 0;
		}
	}
	
	public static void main(String [] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		for (int tc = 1; tc<=n; tc++) {
			sb.append("#" + tc + " ");
			st = new StringTokenizer(br.readLine());
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			A = Integer.parseInt(st.nextToken());
			B = Integer.parseInt(st.nextToken());
			ancestorA = new ArrayList<>();
			ancestorB = new ArrayList<>();
			arr = new Node[V+1];
			for (int i=0; i<V+1; i++) {
				arr[i] = new Node();
			}
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<E; i++) {
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				arr[a].children.add(b);
				arr[b].parents = a;
			}
			find_ancestor(A, ancestorA);
			find_ancestor(B, ancestorB);
			for (int i=0; i<V; i++) {
				if (!ancestorA.get(i).equals(ancestorB.get(i))) break;
				ans = ancestorA.get(i);
			}
			sb.append(ans + " " + dfs(ans));
			sb.append("\n");
			
		}
		System.out.println(sb);
		
	}
	public static int dfs(int parent) {
		int res = 1;
		for (int child : arr[parent].children) {
			res += dfs(child);
		}
		return res;
	}
	public static void find_ancestor(int idx, ArrayList<Integer> ancestor) {
		int parent = arr[idx].parents;
		if (parent != 0) {
			find_ancestor(parent,ancestor);
		}
		ancestor.add(idx);
		
	}
}