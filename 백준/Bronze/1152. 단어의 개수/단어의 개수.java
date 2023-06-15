import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String [] arr = sc.nextLine().split(" ");
		int result = 0;
		for (int i=0; i<arr.length; i++) {
			if (!arr[i].equals("")) {
				result+=1;
			}
		}
		System.out.println(result);
		
		
	}
}