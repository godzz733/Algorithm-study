import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		for (int i=0; i<t; i++) {
			String [] input = br.readLine().split(" ");
			int a = Integer.parseInt(input[0]), b = Integer.parseInt(input[1]), c = Integer.parseInt(input[2]);
			if (a<b-c) {
				System.out.println("advertise");
			} else if (a==b-c) {
				System.out.println("does not matter");
			} else {
				System.out.println("do not advertise");
			}
		}

	}
}