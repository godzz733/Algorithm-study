import java.io.IOException;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
		sc.close();
		if (a*b>c) {
			System.out.println(a*b-c);
		} else {
			System.out.println(0);
		}
	}
}