import java.io.IOException;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i=0; i<t; i++) {
			String str = sc.next();
			char[] arr = str.toCharArray();
			int result = 0;
			int cnt = 1;
			for (int j=0; j<arr.length; j++) {
				if (arr[j]=='X') {
					cnt = 1;
					continue;
				} else {
					result += cnt;
					cnt++;
				}
			}
			System.out.println(result);
		}
		
	}
}