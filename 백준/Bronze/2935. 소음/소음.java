import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = br.readLine();
		String b = br.readLine();
		String c = br.readLine();
		BigInteger a_big = new BigInteger(a);
		BigInteger c_big = new BigInteger(c);
		
		if (b.equals("*")) {
			System.out.println(a_big.multiply(c_big));
		} else {
			System.out.println(a_big.add(c_big));
		}
		
	}
}