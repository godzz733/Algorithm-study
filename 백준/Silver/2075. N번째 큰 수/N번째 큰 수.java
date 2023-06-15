import java.io.*;
import java.util.*;


public class Main{

	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		ArrayList<Integer> arr =new ArrayList<>();
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<n; j++) {
				arr.add(Integer.parseInt(st.nextToken()));
			}
		}
		arr.sort(Comparator.reverseOrder());
		System.out.println(arr.get(n-1));
	
		
		
	}

	
}
