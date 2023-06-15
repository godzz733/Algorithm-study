import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while (true) {
			int [] arr = new int[101];
			int cnt = 0, key = 0;
			String str = br.readLine();
			if (str.equals(".")) {
				break;
			}
			for (int j=0; j<str.length(); j++) {
				if (str.charAt(j)=='(' || str.charAt(j)=='[') {
					arr[cnt] = str.charAt(j);
					cnt++;
				} else if (str.charAt(j)==')') {
					cnt--;
					if (cnt<0) {
						System.out.println("no");
						key ++;
						break;
					}
					else if (arr[cnt]=='(') {
						continue;
					} else {
						System.out.println("no");
						key ++;
						break;
					}
				} else if (str.charAt(j)==']') {
					cnt--;
					if (cnt<0) {
						System.out.println("no");
						key ++;
						break;
					}
					else if (arr[cnt]=='[') {
						continue;
					} else {
						System.out.println("no");
						key ++;
						break;
					}
				}
			}
			if (cnt==0 && key==0) {
				System.out.println("yes");
			} else if(cnt!=0 && key==0) {
				System.out.println("no");
			}
		}
		
	}
}