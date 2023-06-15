import java.io.*;
import java.util.*;


public class Main{

	
	public static void main(String [] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()); 
		int m = Integer.parseInt(st.nextToken());
		int result = Integer.MAX_VALUE;
		int [] arr = new int [n];
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			if (arr[i] >=m) {
				result = 1;
			}
		}
		int sum = arr[0] + arr[1];
		int start = 0;
		int end = 1;
		while (start<=end && end<n) {
			if (sum < m) {
				if (end == n-1) {
					break;
				}
				sum += arr[++end];
			} else {
				result = Math.min(result, end-start+1);
				sum -= arr[start++];
			}
		}
		if (result == Integer.MAX_VALUE) {
			result = 0;
		}
		bw.write(result + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
}