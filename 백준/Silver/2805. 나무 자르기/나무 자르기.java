import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt();
		int [] arr = new int[n];
		for (int i=0; i<n; i++) {
			arr[i] = sc.nextInt();
		}
		sc.close();
		int min = 0, max = 2000000000;
		int result = 0 ;
		while (min<=max) {
			long temp = 0;
			int mid = (min+max)/2;
			for (int i=0; i<n; i++) {
				if (arr[i]-mid>0) {
					temp += arr[i]-mid;
				}
			}
			if (temp<m) {
				max = mid-1;
			} else {
				min = mid+1;
				result = mid;
			}
		}
		System.out.println(result);
		
	}
	

}