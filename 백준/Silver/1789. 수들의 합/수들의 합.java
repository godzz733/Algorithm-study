import java.io.IOException;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		Long n = sc.nextLong();
		sc.close();
		double cnt = Math.sqrt(n*2);
		long result = (long) cnt;
		result-= 2;
		while(true) {
			if (result*(result+1)/2>n) {
				System.out.println(result-1);
				break;
			} else {
				result++;
			}
		}
		
	}
}