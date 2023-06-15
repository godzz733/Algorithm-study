import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		ArrayList arr = new ArrayList();
		for (int i=0; i<n; i++) {
			double a = sc.nextInt();
			arr.add(a);
		}
		arr.sort(Comparator.naturalOrder());
		double max = (double)arr.get(n-1);
		double result = 0;
		for (int i=0; i<n; i++) {
			double a = (double)arr.get(i);
			result += (a/max)*100;
		}
		System.out.println(result/n);
		
	}
}