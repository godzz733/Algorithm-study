import java.io.*;
import java.util.*;

public class Solution {
	static int n;
	static char [] arr;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		for (int tc=1; tc<11; tc++) {
			sb.append("#" + tc + " ");
			n = Integer.parseInt(br.readLine());
			arr = new char[n+1];
			for (int i=1; i<=n; i++) {
				arr[i] = br.readLine().split(" ")[1].charAt(0);
			}
			middle(1);
			sb.append("\n");

		}
		System.out.println(sb);
		
			
	}
	public static void middle(int cur) {
		if (cur>n) return;
		middle(cur*2);
		sb.append(arr[cur]);
		middle(cur*2+1);
		
	}
	
}