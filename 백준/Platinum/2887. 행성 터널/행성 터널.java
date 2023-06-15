import java.io.*;
import java.util.*;

class planet{
	int num,x,y,z;
	planet(int num, int x, int y, int z){
		this.num = num;
		this.x = x;
		this.y = y;
		this.z = z;
	}
}

class edge implements Comparable<edge> {
	int start,end,weight;
	edge(int start, int end, int weight){
		this.start = start;
		this.end = end;
		this.weight = weight;
	}
	
	@Override
	public int compareTo(edge o) {
		return weight - o.weight;
	}
}

public class Main{
	static int [] parent;
	static ArrayList<edge> arr;
	
	public static int find_parent(int x) {
		if (x != parent[x]) {
			parent[x] = find_parent(parent[x]);
		}
		return parent[x];
	}
	public static void union_parent(int a, int b) {
		a = find_parent(a);
		b = find_parent(b);
		if (a<b) {
			parent[b] = a;
		} else {
			parent[a] = b;
		}
	}
	
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		parent = new int [n];
		int result = 0;
		planet [] lst = new planet [n];
		arr = new ArrayList<>();
		for (int i=0; i<n; i++) {
			parent[i] = i;
		}
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken()), y = Integer.parseInt(st.nextToken()), z = Integer.parseInt(st.nextToken());
			lst[i] = new planet(i,x,y,z);
		}
		Arrays.sort(lst,(o1,o2) -> o1.x-o2.x);
		for (int i=0; i<n-1; i++) {
			int weight = Math.abs(lst[i].x-lst[i+1].x);
			arr.add(new edge(lst[i].num,lst[i+1].num,weight));
		}
		Arrays.sort(lst,(o1,o2) -> o1.y-o2.y);
		for (int i=0; i<n-1; i++) {
			int weight = Math.abs(lst[i].y-lst[i+1].y);
			arr.add(new edge(lst[i].num,lst[i+1].num,weight));
		}
		Arrays.sort(lst,(o1,o2) -> o1.z-o2.z);
		for (int i=0; i<n-1; i++) {
			int weight = Math.abs(lst[i].z-lst[i+1].z);
			arr.add(new edge(lst[i].num,lst[i+1].num,weight));
		}
		Collections.sort(arr);
		for (int i=0; i<arr.size(); i++) {
			edge now = arr.get(i);
			if (find_parent(now.start) != find_parent(now.end)) {
				result += now.weight;
				union_parent(now.start,now.end);
			}
		}
		bw.write(result + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
}