import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main{
	
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		int [] dp = new int[n+100];
		String [] str = new String[n+100];
		Arrays.fill(dp, 1000000);
		dp[1] = 0;
		dp[2] = 1;
		dp[3] = 1;
		str[1] = "1";
		str[2] = "2 1";
		str[3] = "3 1";
		for (int i=4; i<n+1; i++) {
			if (i%3 ==0 && i%2==0) {
				dp[i] = Math.min(Math.min(dp[i/3]+1, dp[i/2]+1),dp[i-1]+1);
				if (dp[i]==dp[i/3]+1) str[i] = Integer.toString(i) + " " + str[i/3];
				else if (dp[i]==dp[i/2]+1) str[i] = Integer.toString(i) + " " + str[i/2];
				else str[i] = Integer.toString(i) + " " + str[i-1] ;
			} else if (i%3 ==0 && i%2!=0) {
				dp[i] = Math.min(dp[i/3]+1, dp[i-1]+1);
				if (dp[i]==dp[i/3]+1) str[i] = Integer.toString(i) + " " + str[i/3];
				else str[i] = Integer.toString(i) + " " + str[i-1] ;
			} else if (i%3 !=0 && i%2==0) {
				dp[i] = Math.min(dp[i/2]+1,dp[i-1]+1);
				if (dp[i]==dp[i/2]+1) str[i] = Integer.toString(i) + " " + str[i/2];
				else str[i] = Integer.toString(i) + " " + str[i-1] ;
			} else {
				dp[i] = dp[i-1] +1;
				str[i] = Integer.toString(i) + " " + str[i-1] ;
			}
		}
		System.out.println(dp[n]);
		System.out.println(str[n]);
	}
	
}