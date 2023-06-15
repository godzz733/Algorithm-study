import java.io.IOException;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int temp = n;
		sc.close();
		while (n>1) {
			for (int i=2; i<temp+1; i++) {
				if (n%i==0) {
					n/=i;
					System.out.println(i);
					break;
				}
			}
		}
	}
}