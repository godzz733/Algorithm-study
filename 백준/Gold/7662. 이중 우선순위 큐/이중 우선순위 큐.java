import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeMap;

public class Main{
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		for (int t=0; t<n; t++) {
			int w = Integer.parseInt(br.readLine());
			TreeMap<Integer, Integer> q = new TreeMap<>();
			for (int i =0; i<w; i++) {
				String [] input = br.readLine().split(" ");
				char a = input[0].charAt(0);
				int b = Integer.parseInt(input[1]);
				if (a=='I') {
					q.put(b, q.getOrDefault(b, 0)+1);
				} else {
					if (q.size()==0) {
						continue;
					}
					int num = b==1 ? q.lastKey(): q.firstKey();
					if (q.put(num,q.get(num)-1)==1) {
						q.remove(num);
					}
				}
				
			}
			System.out.println(q.size() == 0 ? "EMPTY" : q.lastKey() + " " + q.firstKey());
		}
	}
}