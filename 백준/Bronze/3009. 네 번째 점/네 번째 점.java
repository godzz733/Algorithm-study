import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		ArrayList arr_a = new ArrayList();
		ArrayList arr_b = new ArrayList();
		for (int i=0; i<3; i++) {
			String a = sc.next(), b = sc.next();
			if (!arr_a.contains(a)) {
				arr_a.add(a);
			} else {
				arr_a.remove(a);
			}
			if (!arr_b.contains(b)) {
				arr_b.add(b);
			} else {
				arr_b.remove(b);
			}
			
		}
		System.out.println(arr_a.get(0) + " " +  arr_b.get(0));
	}
}