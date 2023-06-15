import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		for (int t=0; t<tc; t++) {
			int n = sc.nextInt();
			HashMap<String, Integer> dic = new HashMap<>();
			int result = 1;
			for (int i=0; i<n; i++) {
				String st = sc.next(), str = sc.next();
				if (!dic.containsKey(str)) {
					dic.put(str, 1);
				} else {
					dic.replace(str, dic.get(str) + 1);
				}
			} 
			for (Map.Entry<String, Integer> entry : dic.entrySet()) {
				int value = entry.getValue();
				result *= value +1 ;
			}
			System.out.println(result-1);
			
		}
	}
}
