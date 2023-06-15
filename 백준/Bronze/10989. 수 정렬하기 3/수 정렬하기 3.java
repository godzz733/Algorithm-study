import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter buf = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		int[] arr;
		arr = new int[10001];

		for (int i=0; i<n; i++) {
			int a = Integer.parseInt(br.readLine());
			arr[a] += 1;
		}
		for (int i=0; i<10001; i++) {
			if (arr[i]!=0) {
				for (int j=0; j<arr[i]; j++) {
		            buf.write(String.valueOf(i));
		            buf.write("\n");
				}
				
			}
		}
		buf.close();
	}
}