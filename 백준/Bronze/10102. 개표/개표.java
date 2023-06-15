import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		Integer a = sc.nextInt();
		String str = sc.next();
		int A=0, B=0;
		for (int i=0; i<a; i++) {
			char comp = str.charAt(i);
			if (comp == 'A') {
				A += 1;			
			} else {
				B +=1;
			}
		}
		if (A>B) {
			System.out.println("A");
		} else if (A<B) {
			System.out.println("B");
		} else {
			System.out.println("Tie");
		}
	
		
	}
}