import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	
	static int result,pi[];
	static String find, pattern;
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		find = br.readLine();
		pattern = br.readLine();
		result = 0;
		pi = new int[pattern.length()];
		getpi();
		kmp();
		System.out.println(result);
		
	}
	static void getpi() {
		int j = 0;
		for (int i=1; i<pattern.length(); i++) {
			while (j>0 && pattern.charAt(i) != pattern.charAt(j)) {
				j = pi[j-1];
			}
			if (pattern.charAt(i) == pattern.charAt(j)) {
				pi[i] = ++j;
			}
		}
	}
	static void kmp() {
		int j = 0;
		for (int i=0; i<find.length(); i++) {
			while(j>0 && find.charAt(i) != pattern.charAt(j)) {
				j = pi[j-1];
			}
			if (find.charAt(i) == pattern.charAt(j)) {
				if (j == pattern.length()-1){
					result = 1;
					break;
				} else {
					++j;
				}
			}
		}
	}
}
