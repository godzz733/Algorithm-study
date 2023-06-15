
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;


public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt();

		HashSet<String> set1 = new HashSet<>();
		HashSet<String> set2 = new HashSet<>();
		for (int i=0; i<n; i++) {
			String str = sc.next();
			set1.add(str);
		}
		for (int i=0; i<m; i++) {
			String str = sc.next();
			set2.add(str);
		}
		sc.close();
		set1.retainAll(set2);
		List<String> result = new ArrayList<>(set1);
		Collections.sort(result);
		System.out.println(result.size());
		for (int i=0; i<result.size(); i++) {
			System.out.println(result.get(i));
		}
	}
}
