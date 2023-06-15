import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		while (true) {
			String a = sc.next();
			int key = 0;
			if (a.equals("0")) {
				break;
			} else { 
			for (int i=0; i<a.length()/2; i++) {
				if (a.charAt(i)!=a.charAt(a.length()-i-1)) {
					key += 1;
					System.out.println("no");
					break;
				}
			}
			if (key==0) {
				System.out.println("yes");
			}
			}
		}
	}
}