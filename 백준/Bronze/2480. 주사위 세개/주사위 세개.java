import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int[] dice = {sc.nextInt(),sc.nextInt(),sc.nextInt()};
		sc.close();
		if (dice[0]==dice[1] && dice[1]==dice[2]) {
			System.out.println(10000+dice[0]*1000);
		} else {
			if (dice[0]!=dice[1] && dice[1]!=dice[2] && dice[0]!=dice[2]) {
				Arrays.sort(dice);
				System.out.println(dice[2]*100);
			} else {
				if (dice[0]==dice[1]) {
					System.out.println(1000+dice[0]*100);
				} else if (dice[1]==dice[2]) {
					System.out.println(1000+dice[1]*100);
				} else if (dice[0]==dice[2]) {
					System.out.println(1000+dice[0]*100);
				}
			}
		}
		
	}
}