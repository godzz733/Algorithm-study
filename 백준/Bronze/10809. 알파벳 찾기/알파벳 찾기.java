import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		sc.close();
		for (int i=0; i<26; i++) {
			int key = 0;
			for (int j=0; j<str.length(); j++) {
				if ((str.charAt(j)-'a')==i) {
					System.out.print(j+" ");
					key += 1;
					break;
				}
			}
			if (key==0) {
				System.out.print(-1 + " ");
			}
		}
	}
}