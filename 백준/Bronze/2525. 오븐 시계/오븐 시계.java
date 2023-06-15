import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String [] input = br.readLine().split(" ");
		int h = Integer.parseInt(input[0]), m = Integer.parseInt(input[1]);
		int cook = Integer.parseInt(br.readLine());
		if (m+cook>=60) {
			if ((h+(m+cook)/60)>=24) {
				System.out.print((h+((m+cook))/60)%24+" ");
				System.out.print((m+cook)%60);
			} else {
				System.out.print((h+((m+cook)/60))+" ");
				System.out.print((m+cook)%60);
			}
		} else {
			System.out.print(h+" ");
			System.out.print(m+cook);
		}		
}	
}