import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int key1 = 0, key2=0;
		int [] arr = new int[8];
		for (int i=0; i<8; i++) {
			int a = sc.nextInt();
			arr[i] = a;
		}
		for (int j=1; j<9; j++) {
			if (arr[j-1]!=j) {
				key1 += 1;
				break;
			}
		}
		
		for (int k=8; k>0; k--) {
			if (arr[8-k] != k) {
				key2 += 1;
				break;
			}
		}
		if (key1==0) {
			System.out.println("ascending");
		} else if (key2==0) {
			System.out.println("descending");
		} else {
			System.out.println("mixed");
		}
		
	}
}