
import java.io.IOException;
import java.util.Scanner;

public class Main {
	
	public static int cnt = 1;
	public static int [] arr = new int[10001];
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		int n = sc.nextInt();
		for (int i=0; i<n; i++) {
			String a = sc.next();
			if (a.equals("push")) {
				push(sc.nextInt());
			} else if (a.equals("top")) {
				sb.append(top()).append('\n');
			} else if (a.equals("size")) {
				sb.append(size()).append('\n');
			} else if (a.equals("empty")) {
				sb.append(empty()).append('\n');
			} else if (a.equals("pop")) {
				sb.append(pop()).append('\n');
			}
		}
		System.out.println(sb);
		
	}
	public static void push(int a) {
		arr[cnt] = a;
		cnt++;
	}
	public static int pop(){
		if (cnt == 1) {
			return -1;
		} else {
		int temp = arr[cnt-1];
		arr[cnt-1] = 0;
		cnt--;
		return temp;
		}
	}
	public static int size() {
		return cnt-1;
	}
	public static int empty() {
		if (cnt==1) {
			return 1;
		} else {
			return 0;
		}
	}
	public static int top() {
		if (cnt==1) {
			return -1;
		} else {
		return arr[cnt-1];
		}
	}
}