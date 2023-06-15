import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main{
	static StringTokenizer st;
	static int a,b,c;
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		int [][] arr = new int [n][n];
		for (int i=0; i<n; i++) {
			Arrays.fill(arr[i], 250000000);
		}
		
		int m = Integer.parseInt(br.readLine());
		for (int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			if (arr[a-1][b-1] > c) {
				arr[a-1][b-1] = c;
			}
		}
		for (int k=0; k<n; k++) {
			for (int i=0; i<n; i++) {
				for (int j=0; j<n; j++) {
					arr[i][j] = Math.min(arr[i][j], arr[i][k]+arr[k][j]);
				}
			}
		}
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (arr[i][j] == 250000000 || i == j) {
					if (j!=n-1) {
						sb.append(0).append(" ");
					} else {
						sb.append(0);
					}
				} else {
					if (j!=n-1) {
						sb.append(arr[i][j]).append(" ");
					} else {
						sb.append(arr[i][j]);
					}

				}
			}
			if (i != n-1) {
				sb.append('\n');
			}
		}
		System.out.println(sb);

		
	}
}