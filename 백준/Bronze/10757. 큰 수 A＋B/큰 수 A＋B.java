import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String [] arr = br.readLine().split(" ");
		BigInteger a = new BigInteger(arr[0]);
		BigInteger b = new BigInteger(arr[1]);
		System.out.println(a.add(b));
		
	}
}