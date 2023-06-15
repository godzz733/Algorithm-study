import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String [] arr = br.readLine().split("");
		int result = 10;
		String start = arr[0];
		for (int i=1; i<arr.length; i++) {
			if (start.equals(arr[i])) {
				result += 5;
			} else {
				result += 10;
				start = arr[i];
			}
		}
		System.out.println(result);


	}
}