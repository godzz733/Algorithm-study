import java.io.*;
import java.util.*;

class Pos{
	String name;
	int cnt;
	Pos(String x, int y){
		this.name = x;
		this.cnt = y;
	}
}
class Main {
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		HashMap<String, Integer> map = new HashMap<>();
		ArrayList<String> arr = new ArrayList<>();
		for (int i=0; i<n; i++) {
			String [] inp = br.readLine().split("\\.");
			map.put(inp[1], map.getOrDefault(inp[1], 0)+1);
		}
		Iterator it = map.keySet().iterator();
		while (it.hasNext()) {
			arr.add(it.next().toString());
		}
		Collections.sort(arr);
		for (String x: arr) {
			sb.append(x+" "+map.get(x)).append('\n');
		}
		System.out.println(sb);
		
		
			
	}
	
}