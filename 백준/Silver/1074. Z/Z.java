import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(); 
		int r = sc.nextInt(), c = sc.nextInt();
		System.out.println(Z(n,r,c));
	}
	static int Z(int n, int r, int c) {
		if (n==1) {
			return r*2+c;
		}
		double per = n-1;
		per = Math.pow(2, per);
		int per_int = (int) per;
		if (r<per_int && c<per_int) {
			return Z(n-1,r,c);
		} else if (r<per_int && c>=per_int) {
			int pow = 1;
			for (int i =0; i<n-1; i++) {
				pow *= 4;
			}
			return pow + Z(n-1,r,c%per_int);
		} else if (r>=per_int && c<per_int) {
			int pow = 1;
			for (int i =0; i<n-1; i++) {
				pow *= 4;
			}
			return pow*2 + Z(n-1,r%per_int,c);
		} else {
			int pow = 1;
			for (int i =0; i<n-1; i++) {
				pow *= 4;
			}
			return pow*3 + Z(n-1,r%per_int,c%per_int);
		}
		
	}
}
