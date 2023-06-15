
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int arr[] = {sc.nextInt(), sc.nextInt(), sc.nextInt()};
		sc.close();
		Arrays.sort(arr);
		System.out.println(arr[1]);
	}
}