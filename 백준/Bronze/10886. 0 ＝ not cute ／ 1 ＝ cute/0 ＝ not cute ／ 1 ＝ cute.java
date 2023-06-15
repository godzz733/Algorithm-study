import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		int result = 0;
		for (int i=0; i<t; i++) {
			int a = Integer.parseInt(br.readLine());
			if (a==1) {
				result += 1;
			} else {
				result -= 1;
			}
		}
		if (result<0) {
			System.out.println("Junhee is not cute!");
		} else {
			System.out.println("Junhee is cute!");
		}

	}
}