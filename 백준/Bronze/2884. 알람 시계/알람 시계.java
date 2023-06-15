import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String [] input = br.readLine().split(" ");
		int a = Integer.parseInt(input[0]), b = Integer.parseInt(input[1]);
		if (b-45>=0) {
			System.out.println(a + " " + (b-45));
		} else {
			b = b + 60 - 45;
			if (a-1<0) {
				a = a -1 + 24;
			} else {
				a--;
			} System.out.println(a + " " + b);
		}

	}
}