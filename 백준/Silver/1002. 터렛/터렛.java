import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main{
	
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			double x1 = Double.parseDouble(st.nextToken());
			double y1 = Double.parseDouble(st.nextToken());
			double r1 = Double.parseDouble(st.nextToken());
			double x2 = Double.parseDouble(st.nextToken());
			double y2 = Double.parseDouble(st.nextToken());
			double r2 = Double.parseDouble(st.nextToken());
			double x = Math.sqrt(Math.pow(x1-x2, 2)+Math.pow(y1-y2,2));
			if (x1 == x2 && y1==y2) {
				if (r1 == r2) {
					System.out.println(-1);
				} else {
					System.out.println(0);
				}
			} else if (x == r1+r2 || x+r1 == r2 || x+r2 == r1) {
				System.out.println(1);
			} else if (x > r1+r2 || r2>x+r1 || r1>x+r2) {
				System.out.println(0);
			} else {
				System.out.println(2);
			}
		}
				
	}
}