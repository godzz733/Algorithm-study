import java.awt.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		int [] arr = new int[21];
		int n = sc.nextInt();
		for (int i =0; i<n; i++) {
			switch (sc.next()) {
			case "add":
				int a = sc.nextInt();
				arr[a] = 1;
				break;

			case "remove":
				a = sc.nextInt();
				arr[a] = 0;
				break;

			case "check":
				a = sc.nextInt();
				sb.append(arr[a]).append('\n');
				break;
			
			case "toggle":
				a = sc.nextInt();
				if (arr[a]==1) {
					arr[a] = 0;
				} else {
					arr[a] = 1;
				}
				break;
			case "all":
				for (int j =1; j<21; j++) {
					arr[j] = 1;
				}
				break;
			case "empty":
				for (int j =1; j<21; j++) {
					arr[j] = 0;
				}
				break;
					
		}
			
	}
		System.out.println(sb);
}
}
