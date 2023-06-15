import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
			if (a==0 && b==0 && c==0) {
				break;
			} else {
				int[] arr = new int[3];
				arr[0] = a;
				arr[1] = b;
				arr[2] = c;
				Arrays.sort(arr);
				if (Math.pow(arr[0], 2)+Math.pow(arr[1], 2)==Math.pow(arr[2], 2)) {
					System.out.println("right");
				} else {
					System.out.println("wrong");
				}
			}
		}
		
	}
}