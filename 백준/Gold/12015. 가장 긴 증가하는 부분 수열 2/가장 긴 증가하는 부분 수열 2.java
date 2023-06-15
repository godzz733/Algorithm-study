import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	static int n;
	static int[] arr, dp;
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		arr = new int[n];
		dp = new int[n];
		int LIS = 0;
		for (int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		for (int i=0; i<n; i++) {
			int idx = binary(arr[i], 0, LIS, LIS+1);
			if (idx == -1) {
				dp[LIS++] = arr[i];
			} else {
				dp[idx] = arr[i];
			}
		}
		System.out.println(LIS);
	}
	static int binary(int num, int st, int end, int size) {
		int result = 0;
		while (st<=end) {
			int mid = (st+end)/2;
			if (num<=dp[mid]) {
				end = mid - 1;
				result = mid;
			} else {
				st = mid + 1;
			}
		}
		if (st == size) {
			return -1;
		} else {
			return result;
		}
	}

}
