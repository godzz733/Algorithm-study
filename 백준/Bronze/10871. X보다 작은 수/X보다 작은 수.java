import java.io.IOException;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b= sc.nextInt();
		for (int i=0; i<a; i++) {
			int c = sc.nextInt();
			if (c<b) {
				System.out.print(c+" ");
			}
		}	
	}
}