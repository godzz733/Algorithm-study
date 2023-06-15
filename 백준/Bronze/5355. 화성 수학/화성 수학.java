import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		for (int i=0; i<n; i++) {
			String [] input = br.readLine().split(" ");
			double a = Double.parseDouble(input[0]);
			for (int j=1; j<input.length; j++) {
				String str = input[j];
				if (str.equals("@")) {
					a = a * 3;
				} else if (str.equals("%")) {
					a = a + 5;
				} else {
					a = a - 7;
				}

			}
			System.out.printf(("%.2f"),a);
			System.out.println(" ");
			
			
		}
	}
}