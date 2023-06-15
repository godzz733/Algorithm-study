import java.io.*;
import java.util.*;


public class Main{

	
	public static void main(String [] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()); 
		int result = 0;
		if (n!=1) {
		boolean [] prime = new boolean[n+2];
		prime[1] = true;
		ArrayList<Integer> primes = new ArrayList<>();
		for (int i = 2; i<n+1; i++) {
			if (prime[i]) continue;
			primes.add(i);
			prime[i] = true;
			for (int j = i*2; j<n+1; j += i ) {
				prime[j] = true;
			}
		}
		int sum = primes.get(0);
		int start = 0, end = 0;
		while (start<=end && end<primes.size()) {
			if (sum < n) {
				if (end == primes.size()-1) break;
				sum += primes.get(++end);
			} else {
				if (sum == n) result++;
				sum -= primes.get(start++);
			}
		}
		}
		bw.write(result + "\n");
		bw.flush();
		bw.close();
		br.close();
		
	}
}