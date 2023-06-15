import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		while (true) {
			st = new StringTokenizer(br.readLine());
			String result;
			int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());
			if (a == 0) break;
			int [] arr = new int [3];
			arr[0] = a;
			arr[1] = b;
			arr[2] = c;
			Arrays.sort(arr);
			if (arr[0] + arr[1] <= arr[2]) result = "Invalid";
			else {
				if (arr[0] == arr[1] && arr[1] == arr[2]) result = "Equilateral";
				else if (arr[0] == arr[1] || arr[1] == arr[2] || arr[0] == arr[2]) result = "Isosceles";
				else result = "Scalene";
			}
			bw.write(result + "\n");
		}
		bw.flush();
		bw.close();
		br.close();


			
	}
	
}