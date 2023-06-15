import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int k = sc.nextInt(), result = 0, cnt = 0;
		int [] arr = new int[k];
		for (int i=0; i<k; i++) {
			int a = sc.nextInt();
			if (a!=0) {
				arr[cnt] = a;
				cnt += 1;
			} else {
				cnt -=1 ;
				arr[cnt] = 0;
			}
		}
		for (int i=0; i<k; i++) {
			result += arr[i];
		}
		System.out.println(result);
		
	}
}