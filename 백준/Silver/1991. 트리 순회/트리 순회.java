import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main{
	static String [] l;
	static String [] r;
	static String [] p;
	static StringBuilder sb1,sb2,sb3;
	static void pre(int x) {
		sb1.append(p[x]);
		if (!l[x].equals(".")) {
			pre(l[x].charAt(0)-'A'+1);
		}
		if (!r[x].equals(".")) {
			pre(r[x].charAt(0)-'A'+1);
		}
	}
	static void mid(int x) {
		if (!l[x].equals(".")) {
			mid(l[x].charAt(0)-'A'+1);
		}
		sb2.append(p[x]);
		if (!r[x].equals(".")) {
			mid(r[x].charAt(0)-'A'+1);
		}
	}
	static void post(int x) {
		if (!l[x].equals(".")) {
			post(l[x].charAt(0)-'A'+1);
		}
		if (!r[x].equals(".")) {
			post(r[x].charAt(0)-'A'+1);
		}
		sb3.append(p[x]);
	}
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		l = new String[n+1];
		r = new String[n+1];
		p = new String[n+1];
		sb1 = new StringBuilder();
		sb2 = new StringBuilder();
		sb3 = new StringBuilder();
		for (int i=0; i<n; i++) {
			String [] input = br.readLine().split(" ");
			int a = input[0].charAt(0)-'A'+1;
			l[a] = input[1];
			r[a] = input[2];
			p[a] = input[0];
		}
		pre(1);
		mid(1);
		post(1);
		System.out.println(sb1);
		System.out.println(sb2);
		System.out.println(sb3);
	}
}