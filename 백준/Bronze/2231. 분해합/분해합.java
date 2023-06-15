import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int key=0;
		for (int i=x-60; i<x; i++) {
			String temp = Integer.toString(i);
			int result = i;
			for (int j=0; j<temp.length(); j++) {
				result += (temp.charAt(j)-'0');
			}
			if (result == x) {
				System.out.println(i);
				key += 1;
				break;
			}
		}
		if (key==0) {
			System.out.println(0);
		}
		
	}
}