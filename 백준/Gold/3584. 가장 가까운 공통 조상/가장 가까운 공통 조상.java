import java.io.*;
import java.util.*;

public class Main {
	static public class Node{
		int parent;
		List<Integer> children;
		Node(){
			this.children = new ArrayList<Integer>();
			this.parent = 0;
		}
	}
	static Node [] arr;
	static int V, ans;
	static ArrayList<Integer> ancestorA, ancestorB;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		for (int tc=0; tc<n; tc++) {
			V = Integer.parseInt(br.readLine());
			ancestorA = new ArrayList<>();
			ancestorB = new ArrayList<>();
			arr = new Node[V+1];
			for (int i=0; i<V+1; i++) {
				arr[i] = new Node();
			}
			for (int i=0; i<V-1; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken());
				arr[a].children.add(b);
				arr[b].parent = a;
			}
			st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken()), B = Integer.parseInt(st.nextToken());
			find_ancestor(A, ancestorA);
			find_ancestor(B, ancestorB);
			ancestorA.add(A);
			ancestorB.add(B);
			for (int i=0; i<V; i++) {
				if (!ancestorA.get(i).equals(ancestorB.get(i))) break;
				ans = ancestorA.get(i);
			}
			sb.append(ans + "\n");
		}
		System.out.println(sb);
			
	}
	public static void find_ancestor(int idx, ArrayList<Integer> ancestor) {
		int parent = arr[idx].parent;
		if (parent != 0) {
			find_ancestor(parent, ancestor);
		}
		ancestor.add(idx);
	}
	
}