import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main{
	static int n,m;
	static int [] arr;
	static ArrayList<Integer> a,b;
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n];
		long result = 0;
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		a = new ArrayList<>();
		b = new ArrayList<>();
		a_sum(0,0);
		b_sum(n/2,0);
		Collections.sort(a);
		Collections.sort(b);

		int a_num = 0, b_num = b.size()-1;
		while (a_num<a.size() && b_num>=0) {
			if (a.get(a_num)+b.get(b_num)==m) {
				int temp = a.get(a_num);
				long cnt1 = 0;
				long cnt2 = 0;
				while (a_num<a.size() && a.get(a_num)==temp) {
					cnt1++;
					a_num++;
				}
				temp = b.get(b_num);
				while (b_num>=0 && b.get(b_num)==temp) {
					cnt2++;
					b_num--;
				}
				result += cnt1*cnt2;
			}
			else if (a.get(a_num)+b.get(b_num)>m) {
				b_num--;
			} else {
				a_num++;
			}
			
		}
		if (m==0) {
			result--;
		}
		System.out.println(result);
		
		
	}
	static void a_sum(int idx, int sum) {
		if (idx==n/2) {
			a.add(sum);
			return;
		}
		a_sum(idx+1, sum+arr[idx]);
		a_sum(idx+1,sum);
	}
	static void b_sum(int idx, int sum) {
		if (idx==n) {
			b.add(sum);
			return;
		}
		b_sum(idx+1, sum+arr[idx]);
		b_sum(idx+1,sum);
	}
	
	
}
		