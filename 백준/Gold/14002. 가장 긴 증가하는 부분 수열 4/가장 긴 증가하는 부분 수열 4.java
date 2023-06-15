import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	static class pos{
		int x,y;
		String cnt;
		public pos(int x, int y, String cnt) {
			this.x = x;
			this.y = y;
			this.cnt = cnt;
		}
	}
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		br.close();
		int [] arr = new int[n];
		pos [] dp = new pos[n];
		for (int i=0; i<n; i++) {
			dp[i] = new pos(0,0,"");
		}
		for (int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int result = 0;
		String result_cnt = "";
		for (int i=0; i<n; i++) {
			dp[i].x = 1;
			dp[i].y = arr[i];
			dp[i].cnt = Integer.toString(arr[i]);
			for (int j=0; j<i; j++) {
				if (arr[i]>arr[j]) {
					if (dp[i].x < (dp[j].x)+1) {
						dp[i].x = dp[j].x+1;
						dp[i].cnt = dp[j].cnt + " " + Integer.toString(arr[i]);
						if (result<dp[i].x) {
							result=dp[i].x; result_cnt = dp[i].cnt;
						}
					}
				}
			}
		}
		if (result ==0) {
			System.out.println(1);
			System.out.println(arr[0]);
		} else {
		System.out.println(result);
		System.out.println(result_cnt);
		}
	}


}