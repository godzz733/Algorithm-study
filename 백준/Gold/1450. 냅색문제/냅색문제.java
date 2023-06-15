import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main{
	static int n,m;
	static int [] arr;
	static ArrayList<Integer> a_arr, b_arr;
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		int result = 0;
		st = new StringTokenizer(br.readLine());
		arr = new int[n+1];
		for (int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		br.close();
		a_arr = new ArrayList<>();
		b_arr = new ArrayList<>();
		a_sum(0,0);
		b_sum(n/2,0);
		Collections.sort(b_arr);
		for (int i=0; i<a_arr.size(); i++) {
			result += binary(a_arr.get(i))+1;
		}
		System.out.println(result);
		
	}
	static void a_sum(int idx, int sum) {
		if (sum>m) {
			return;
		}
		if (idx==n/2) {
			a_arr.add(sum);
			return;
		}
		a_sum(idx+1,sum+arr[idx]);
		a_sum(idx+1,sum);
	}
	static void b_sum(int idx, int sum) {
		if (sum>m) {
			return;
		}
		if (idx==n) {
			b_arr.add(sum);
			return;
		}
		b_sum(idx+1,sum+arr[idx]);
		b_sum(idx+1,sum);
	}
	static int binary(int cnt) {
		int st = 0;
		int end = b_arr.size()-1;
		int idx = 0;
		while (st<=end) {
			int mid = (st+end)/2;
			if (cnt + b_arr.get(mid) > m ) {
				end = mid-1;
			} else {
				st = mid+1;
				idx = mid;
			}
		}
		return idx;
	}
}
		