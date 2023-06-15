import java.io.*;
import java.util.*;
class pos{
	int to, time;
	pos(int to, int time){
		this.to = to;
		this.time = time;
	}
}

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken()), r = Integer.parseInt(st.nextToken());
		int [] road = new int [n+1];
		st = new StringTokenizer(br.readLine());
		for (int i=1; i<n+1; i++) {
			road[i] = Integer.parseInt(st.nextToken());
		}
		int [][] arr = new int[n+1][n+1];
		for (int i=0; i<n+1; i++) {
			Arrays.fill(arr[i], 987654321);
			arr[i][i] = 0;
		}
		for (int i=0; i<r; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());
			arr[a][b] = Math.min(arr[a][b], c);
			arr[b][a] = Math.min(arr[a][b], c);
		}
		for (int k=1; k<n+1; k++) {
			for (int i=1; i<n+1; i++) {
				for (int j=0; j<n+1; j++) {
					arr[i][j] = Math.min(arr[i][j], arr[i][k]+arr[k][j]);
				}
			}
		}
		int result = 0;
		for (int i=1; i<n+1; i++) {
			int tem = 0;
			for (int j=1; j<n+1; j++) {
				if (arr[i][j]<=m) tem+=road[j];
			}
			result = Math.max(result,tem);
		}
		bw.write(result + "\n");
		bw.flush();
		bw.close();
		br.close();


			
	}
	
}