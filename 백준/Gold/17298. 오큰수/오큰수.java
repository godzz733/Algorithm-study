import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Array;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Deque;
import java.util.LinkedList;
import java.util.PriorityQueue;

public class Main{
	static class pos{
		int a,b;
		public pos(int a,int b) {
			this.a = a;
			this.b = b;
		}
	}
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		int n = Integer.parseInt(br.readLine());
		int [] arr = new int [n];
		int [] result = new int [n];
		Arrays.fill(result, -1);
		String [] tem = br.readLine().split(" ");
		for (int i=0; i<tem.length; i++) {
			arr[i] = Integer.parseInt(tem[i]);
		}
		Deque<pos> q = new ArrayDeque();
		int _min = Integer.MAX_VALUE;
		for (int i=0; i<n; i++) {
			if (arr[i]<_min) {
				_min = arr[i];
				q.addLast(new pos(arr[i],i));
			} else {
				while (!q.isEmpty() && q.peekLast().a<arr[i]) {
					pos cur = q.pollLast();
					result[cur.b] = arr[i];
				}
				q.add(new pos(arr[i],i));
				_min = arr[i];
			}
		}
		for (int i =0; i<n; i++) {
			sb.append(result[i]).append(" ");
		}
		System.out.println(sb);
	}

}