import java.util.HashMap;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt();
		StringBuilder sb = new StringBuilder();
		HashMap<String, String> dic = new HashMap<>();
		for (int i=0; i<n; i++) {
			String url = sc.next(), pass = sc.next();
			dic.put(url, pass);
			
		}
		for (int i=0; i<m; i++) {
			String result = sc.next();
			sb.append(dic.get(result)).append('\n');
		}
		sc.close();
		System.out.println(sb);
	}
}
