import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int [] arr = new int[12];
		arr[1] = 1;
		arr[2] = 2;
		arr[3] = 4;
		for (int i=4; i<11; i++) {
			arr[i] = arr[i-1]+arr[i-2]+arr[i-3];
		}
		int n = sc.nextInt();
		for (int i=0; i<n; i++) {
			int a = sc.nextInt();
			System.out.println(arr[a]);
		}
	}
}