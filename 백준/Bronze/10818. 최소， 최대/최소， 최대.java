import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		String [] arr = br.readLine().split(" ");
		int [] result = new int[a];
		int i = 0;
		for (String num: arr) {
			result[i] = Integer.parseInt(num);
			i ++;
		}
		Arrays.sort(result);
		System.out.println(result[0] + " " + result[a-1]);
		
		
	}
}