import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt();
		int [] arr = new int[n];
		int max = 1000000000, result =0, cnt = 0;
		for (int i=0; i<n; i++) {
			int a = sc.nextInt();
			arr[i] = a;
		}
		for (int i=0; i<n-2; i++) {
			result += arr[i];
			for (int j=i+1; j<n-1; j++) {
				result += arr[j];
				for (int k=j+1; k<n; k++) {
					result += arr[k];
					if (Math.abs(result-m)<max && result<=m) {
						cnt = result;
						max = Math.abs(result-m);
					}
					result -= arr[k];
				}
				result -= arr[j];
			}
			result -= arr[i];
		}
		System.out.println(cnt);
		
	}
}