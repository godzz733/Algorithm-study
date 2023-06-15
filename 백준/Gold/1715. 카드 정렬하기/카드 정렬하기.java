import java.io.*;
import java.util.*;


public class Main{

	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> q = new PriorityQueue<>();
		for (int i=0; i<n; i++) {
			int tem = Integer.parseInt(br.readLine());
			q.add(tem);
		}
		int result = 0;
		while (q.size() != 1) {
			int a = q.poll();
			int b = q.poll();
			q.add(a+b);
			result += a+b;
		}
		System.out.println(result);
		
		
	}

	
}
