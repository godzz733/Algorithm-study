import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main{

	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		long result = 0;
		int [] a = new int[n];
		int [] b = new int[n];
		int [] c = new int[n];
		int [] d = new int[n];
		int [] ab = new int[n*n];
		int [] cd = new int[n*n];
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			a[i] = Integer.parseInt(st.nextToken());
			b[i] = Integer.parseInt(st.nextToken());
			c[i] = Integer.parseInt(st.nextToken());
			d[i] = Integer.parseInt(st.nextToken());
		}
		int cnt = 0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				ab[cnt] = a[i]+b[j];
				cd[cnt++] = c[i]+d[j];
			}
		}
		Arrays.sort(ab);
		Arrays.sort(cd);
		int left = 0, right = n*n-1;
		while (left<n*n && right>=0) {
			if (ab[left]+cd[right]>0) {
				right--;
			} else if (ab[left]+cd[right]<0) {
				left++;
			} else {
				long cnt1=0, cnt2=0;
				int temp = ab[left];
				while (left<n*n && ab[left]==temp) {
					left++;
					cnt1++;
				}
				temp = cd[right];
				while (right>=0 && cd[right]==temp) {
					right--;
					cnt2++;
				}
				result += cnt1*cnt2;
			}
		}
		System.out.println(result);
		
		
	}



}
	
	

		