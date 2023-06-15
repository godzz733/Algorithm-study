import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.StringTokenizer;

public class Main{
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		ArrayList<HashSet<Integer>> lst = new ArrayList<>();
		for (int i=0; i<m; i++) {
			lst.add(new HashSet<Integer>());
		}
		Set<Integer> set = new HashSet<>();
		st = new StringTokenizer(br.readLine());
		int tem = Integer.parseInt(st.nextToken());
		for (int i=0; i<tem; i++) {
			set.add(Integer.parseInt(st.nextToken()));
		}
		
		for (int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			tem = Integer.parseInt(st.nextToken());
			for (int j=0; j<tem; j++) {
				lst.get(i).add(Integer.parseInt(st.nextToken()));
			}
			Iterator<Integer> it = set.iterator();
			while (it.hasNext()) {
				if (lst.get(i).contains(it.next())) {
					set.addAll(lst.get(i));
					break;
				}
			}
		}
		for (int i=0; i<50; i++) {
			for (int j=0; j<m; j++) {
				Iterator<Integer> it = set.iterator();
				while (it.hasNext()) {
					if (lst.get(j).contains(it.next())) {
						set.addAll(lst.get(j));
						break;
					}
				}
			}
		}
		int result = m;
		for (int i=0; i<m; i++) {
			Iterator<Integer> it = set.iterator();
			while (it.hasNext()) {
				if (lst.get(i).contains(it.next())) {
					result--;
					break;
				}
			}
		}
		Iterator<Integer> a = set.iterator();
		System.out.println(result);
	}
}