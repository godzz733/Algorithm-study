import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int [] arr = new int[1002];
		arr[1] = 1;
		arr[2] = 3;
		for (int i=3; i<1001; i++) {
			arr[i] = (arr[i-2]*2 + arr[i-1])%10007;
		}
		int a = sc.nextInt();
		System.out.println(arr[a]);
	}
}