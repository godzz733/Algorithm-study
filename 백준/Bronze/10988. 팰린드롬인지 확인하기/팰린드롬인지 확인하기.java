import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		sc.close();
		StringBuffer sb = new StringBuffer(str);
		String result = sb.reverse().toString();
		if (str.equals(result)) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
		
	}
}