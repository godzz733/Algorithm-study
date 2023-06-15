import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main{
	static String [] a;
	static String com;
	static int num;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		int n = Integer.parseInt(br.readLine());
		int [] arr = new int[10000];
		Arrays.fill(arr, -1);
		int now = 0;
		int front = 0;
		for (int i=0; i<n; i++) {
			a = br.readLine().split(" ");
			com = a[0];
			if (com.equals("push")) {
				num = Integer.parseInt(a[1]);
			}
			if (com.equals("push")) {
				arr[now++] = num;
			} else if (com.equals("front")) {
				if (front==now) {
					sb.append(-1).append('\n');
					continue;
				}
				sb.append(arr[front]).append('\n');
			} else if (com.equals("back")) {
				if (front==now) {
					sb.append(arr[front]).append('\n');
					continue;
				}
				sb.append(arr[now-1]).append('\n');
			} else if (com.equals("size")) {
				sb.append(now-front).append('\n');
			} else if (com.equals("empty")) {
				if (front==now) {
					sb.append(1).append('\n');
				} else {
					sb.append(0).append('\n');
				}
			} else {
				if (front==now) {
					sb.append(-1).append('\n');
				} else {
					sb.append(arr[front]).append('\n');
					arr[front++] = -1;
				}
			}
		}
		System.out.println(sb);
	}

}