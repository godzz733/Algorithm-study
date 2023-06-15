import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for (int i=0; i<n; i++) {
			int [] arr = new int[50];
			int cnt = 0, key = 0;
			String str = sc.next();
			for (int j=0; j<str.length(); j++) {
				if (str.charAt(j)=='(' || str.charAt(j)=='[') {
					arr[cnt] = str.charAt(j);
					cnt++;
				} else if (str.charAt(j)==')') {
					cnt--;
					if (cnt<0) {
						System.out.println("NO");
						key ++;
						break;
					}
					else if (arr[cnt]=='(') {
						continue;
					} else {
						System.out.println("NO");
						key ++;
						break;
					}
				} else {
					cnt--;
					if (cnt<0) {
						System.out.println("NO");
						key ++;
						break;
					}
					else if (arr[cnt]=='[') {
						continue;
					} else {
						System.out.println("NO");
						key ++;
						break;
					}
				}
			}
			if (cnt==0) {
				System.out.println("YES");
			} else if(cnt!=0 && key==0) {
				System.out.println("NO");
			}
		}
		
	}
}