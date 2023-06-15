import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String [] input = br.readLine().split(" ");
		int h = Integer.parseInt(input[0]), m = Integer.parseInt(input[1]), s = Integer.parseInt(input[2]);
		int cook = Integer.parseInt(br.readLine());
		if (s+cook>=60) {
			if (m+((s+cook)/60)>=60) {
				if (h+(m+((s+cook)/60))/60>=24) {
					System.out.println((h+(m+((s+cook)/60))/60)%24 + " " + (m+((s+cook)/60))%60 + " " + (s+cook)%60);
				} else {
					System.out.println((h+(m+((s+cook)/60))/60) + " " + (m+((s+cook)/60))%60 + " " + (s+cook)%60);
				}
				
			} else {
				System.out.println(h + " " + (m+((s+cook)/60)) + " " + (s+cook)%60);
			}
			
		} else {
			System.out.println(h + " " + m + " " + (s+cook));
		}
	}
}