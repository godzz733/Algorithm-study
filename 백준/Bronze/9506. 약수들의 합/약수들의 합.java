import java.io.IOException;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		while (true) {
			int a = sc.nextInt();
			int temp = a;
			int result = 1;
			String re = temp + " = " + "1 ";
			if (a==-1) {
				break;
			} else {
				int i=2;
				while (i<=a/2) {
					if (a%i==0) {
						if (i!=temp) {
							result += i;
							re += "+ " + i + " ";
						i++;	
						}
					} else {
						i ++;
					}
				}
			}
			if (result==temp) {
				System.out.println(re);
			} else {
				System.out.println(temp + " is NOT perfect.");
			}
		}
		
	}
}