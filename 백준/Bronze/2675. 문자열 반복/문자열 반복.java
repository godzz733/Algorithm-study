import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.ArrayList;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		for (int i=0; i<n; i++) {
			String result = "";
			String [] input = br.readLine().split(" ");
			int a = Integer.parseInt(input[0]);
			char[] characterArray = input[1].toCharArray();
			for(char c : characterArray) {
				for(int j=0; j<a; j++) {
					result += c;
				}

			}
			System.out.println(result);
			
			
			
		}
	}
}