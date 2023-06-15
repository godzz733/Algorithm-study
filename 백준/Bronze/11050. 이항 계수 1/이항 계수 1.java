import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt(), c = a-b;
		int result = 0;
		result += factorial(a)/(factorial(b)*factorial(c));
		System.out.println(result);
	}
	public static int factorial(int n) {
	    if (n == 1 || n==0) {
	        return 1;
	    } else {
	        return n * factorial(n-1);
	    }
	}

}