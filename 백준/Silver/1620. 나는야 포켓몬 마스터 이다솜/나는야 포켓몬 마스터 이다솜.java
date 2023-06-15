import java.util.HashMap;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt();
		StringBuilder sb = new StringBuilder();
		HashMap<String, String> dic = new HashMap<>();
		for (int i =0; i<n; i++) {
			String name = sc.next();
			String num = Integer.toString(i+1);
			dic.put(name, num);
			dic.put(num, name);
		}
		for (int i =0; i<m; i++) {
			sb.append(dic.get(sc.next())).append('\n');
		}
		sc.close();
		System.out.println(sb);
	}
}
