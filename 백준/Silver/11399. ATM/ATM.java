
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> arr = new ArrayList<>();
		int n = sc.nextInt();
		int result = 0 ;
		int [] lst = new int[n];
		for (int i =0; i<n; i++) {
			arr.add(sc.nextInt());
		}
		sc.close();
		Collections.sort(arr);
		lst[0] = arr.get(0);
		for (int i =1; i<n; i++) {
			lst[i] = lst[i-1] + arr.get(i);
		}
		result = Arrays.stream(lst).sum();
		System.out.println(result);
		
	}
}
