import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int result = 0;
		for (int i=0; i<5; i++) {
			int t = Integer.parseInt(br.readLine());
			if (t<40) {
				result += 40;
				continue;
			}
			result += t;
		}
		System.out.println(result/5);
		
	}
}