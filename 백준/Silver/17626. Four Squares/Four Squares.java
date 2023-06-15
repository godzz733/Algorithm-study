import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int [] arr = new int[50626];
		for (int i =0; i<50626; i++) {
			arr[i] = 100000000;
		}
		for (int i=1; i<226; i++) {
			arr[i*i] = 1;
		}
		for (int i=1; i<226; i++) {
			for (int j=1; j<50001; j++) {
				if (j+i*i<=50001) {
					arr[j+i*i] = Math.min(arr[j+i*i], arr[j]+1);
				}
			}
		}
		int a = sc.nextInt();
		System.out.println(arr[a]);
	}
}