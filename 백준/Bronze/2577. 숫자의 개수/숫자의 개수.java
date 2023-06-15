import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
		int num = a*b*c;
		String str = Integer.toString(num);
		int [] arr = new int[10];
		for (int i=0; i<str.length(); i++) {
//			System.out.println(str.charAt(i));
			arr[str.charAt(i)-'0'] += 1;
		}
		for (int j=0; j<10; j++ ) {
			System.out.println(arr[j]);
		}
		
		
	}
}