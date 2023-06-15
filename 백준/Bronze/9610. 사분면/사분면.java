import java.io.IOException;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int Q1=0, Q2=0, Q3=0, Q4=0, AXIS=0;
		for (int i=0; i<t; i++) {
			int a = sc.nextInt(), b = sc.nextInt();
			if (a==0 || b==0) {
				AXIS += 1;
			} else if (a>0 && b>0) {
				Q1 += 1;
			} else if (a>0 && b<0) {
				Q4 += 1;
			} else if (a<0 && b>0) {
				Q2 += 1;
			} else {
				Q3 += 1;
			}
		}
		System.out.println("Q1: " +  Q1);
		System.out.println("Q2: " +  Q2);
		System.out.println("Q3: " +  Q3);
		System.out.println("Q4: " +  Q4);
		System.out.println("AXIS: " +  AXIS);
		
	}
}