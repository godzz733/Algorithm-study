import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt();
		int [] arr = new int[b+100];
		StringBuilder sb = new StringBuilder();
		for (int i=2; i<b+1; i++) {
			if (arr[i]==0 && i<=b) {
				if (i>=a) {
				sb.append(i).append('\n');}
				for (int j=i; j<b+1; j+=i) {
					arr[j] = 1;
				}
			}
		}
		System.out.println(sb);
	}
	

}