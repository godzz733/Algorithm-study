import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList arr = new ArrayList();
		for (int i=0; i<10; i++) {
			int a = sc.nextInt()%42;
			if (!arr.contains(a)) {
				arr.add(a);
			}
		}
		System.out.println(arr.size());
	}
}