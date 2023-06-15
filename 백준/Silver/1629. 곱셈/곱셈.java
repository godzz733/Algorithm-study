import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	static long a,b,c;
	
	static long mul(long a, long b, long c) {
		if (b==1) return a%c;
		
		long temp = mul(a,b/2,c);
		
		if (b%2==1) return (temp*temp%c) * a % c;
		return temp*temp%c;
		
	}
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		System.out.println(mul(a,b,c));
		
	}
	
}