import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = sc.nextInt();
		String [][] arr = new String[n][2];
		for (int i=0; i<n; i++) {
			arr[i][0] = sc.next();
			arr[i][1] = sc.next();
		}
		Arrays.sort(arr, new Comparator<String[]>() {
			@Override
			public int compare(String[] o1,String[] o2) {
				return Integer.parseInt(o1[0]) - Integer.parseInt(o2[0]);
			}
		});
		for (int i=0; i<n; i++) {
			System.out.println(arr[i][0] + " " + arr[i][1]);
		}
			
		
	}
}