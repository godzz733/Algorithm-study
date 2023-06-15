import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int a = 0, b=0, c=0, key=0;
		while (n>0) {
			if (n-300>=0) {
				n-=300;
				a++;
			} else if (n-60>=0) {
				n-=60;
				b++;
			} else if (n-10>=0) {
				n-=10;
				c++;
			} else {
				key++;
				break;
			}
		}
		if (key==1) {
			System.out.println(-1);
		} else {
		System.out.println(a + " " + b + " " + c);
		}
	}
}