import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main{

		
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		ArrayList<ArrayList<Integer>> arr = new ArrayList<ArrayList<Integer>>();
		int n = Integer.parseInt(br.readLine());
		int result = 1;
		for (int i=0; i<n; i++) {
			arr.add(new ArrayList<Integer>());
		}
		for (int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j=0; j<i+1; j++) {
				arr.get(i).add(Integer.parseInt(st.nextToken()));
			}
		}
		for (int i=1; i<n; i++) {
			arr.get(i).set(0, arr.get(i-1).get(0)+arr.get(i).get(0));
		}
		for (int i=1; i<n; i++) {
			arr.get(i).set(i, arr.get(i-1).get(i-1)+arr.get(i).get(i));
		}
		if (n>1) {
		for (int i=2; i<n; i++) {
			for (int j=1; j<i; j++) {
				arr.get(i).set(j, Math.max(arr.get(i-1).get(j-1), arr.get(i-1).get(j))+arr.get(i).get(j));
			}
		}
		for (int i=0; i<n; i++) {
			if (arr.get(n-1).get(i)>result) {
				result = arr.get(n-1).get(i);
			}
		}
		System.out.println(result);
	} else {
		System.out.println(arr.get(0).get(0));
	}
	}
}