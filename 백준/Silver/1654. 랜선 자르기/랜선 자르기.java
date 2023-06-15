import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = sc.nextInt(), b = sc.nextInt();
		int [] arr = new int[a];
		long result = 0;
		for (int i=0; i<a; i++) {
			arr[i] = sc.nextInt();
		}
		sc.close();
		long min=1, max=9223372036854775800L;
		while (min<=max) {
			long mid = (min+max)/2;
			long temp = 0;
			for (int i=0; i<a; i++) {
				temp += arr[i]/mid;
			}
			if (temp<b) {
				max = mid-1;
			} else {
				min = mid + 1;
				result = mid;
			}
		}
		System.out.println(result);
	}
	

}