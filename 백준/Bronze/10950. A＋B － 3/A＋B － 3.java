import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		for (int i =1; i<a+1; i++) {
			int b=sc.nextInt(), c=sc.nextInt();
			System.out.println(b+c);
		}
		
	}
}