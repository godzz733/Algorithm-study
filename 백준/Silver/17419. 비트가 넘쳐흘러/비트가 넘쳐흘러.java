import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int k = Integer.parseInt(br.readLine());
		long result = Long.parseLong(br.readLine(),2);
		int cnt = 0;
		while (result>0) {
			cnt++;
			result = result-(result&((~result)+1));
		}
		System.out.println(cnt);
	}
}
