import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int result = 0;
		int n = sc.nextInt();
		for (int i=0; i<n; i++) {
			int a = 0;
			int[] dice = {sc.nextInt(),sc.nextInt(),sc.nextInt()};
			if (dice[0]==dice[1] && dice[1]==dice[2]) {
				a=(10000+dice[0]*1000);
			} else {
				if (dice[0]!=dice[1] && dice[1]!=dice[2] && dice[0]!=dice[2]) {
					Arrays.sort(dice);
					a=(dice[2]*100);
				} else {
					if (dice[0]==dice[1]) {
						a=(1000+dice[0]*100);
					} else if (dice[1]==dice[2]) {
						a=(1000+dice[1]*100);
					} else if (dice[0]==dice[2]) {
						a=(1000+dice[0]*100);
					}
				}
			}
			if (result<a) {
				result = a;
			}
		}
		System.out.println(result);
	}
}