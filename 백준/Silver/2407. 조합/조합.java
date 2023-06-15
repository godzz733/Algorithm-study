import java.math.BigInteger;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt();
		BigInteger result = BigInteger.ONE;
		for (int i=n; i>Math.max(n-m,m); i--) {
			result = result.multiply(new BigInteger(String.valueOf(i)));
		}
		for (int i = 1; i<Math.min(n-m, m)+1;i++) {
			result = result.divide(new BigInteger(String.valueOf(i)));
		}
		System.out.println(result);
	}
}