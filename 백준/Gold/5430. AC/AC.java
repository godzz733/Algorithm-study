import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;


public class Main{

	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		for (int i=0; i<n; i++) {
			String [] command = br.readLine().split("");
			int m = Integer.parseInt(br.readLine());
			String lst = br.readLine();
			String tem = lst.substring(1,lst.length()-1);
			String [] arr = tem.split(",");
			Deque<Integer> q = new ArrayDeque<>();
			if (m != 0) {
				for (int j=0; j<arr.length; j++) {
					q.add(Integer.parseInt(arr[j]));
				}
			}
			int rdd = 0;
			int err = 0;
			sb = new StringBuilder();
			sb.append("[");
			for (int j=0; j<command.length; j++) {
				if (command[j].equals("D")) {
					if (q.size() == 0) {
						err = 1;
						break;
					} else {
						if (rdd == 0) {
							q.poll();
						} else {
							q.pollLast();
						}
					}
			
				} else {
					if (rdd == 0) {
						rdd = 1;
					} else {
						rdd = 0;
					}
				}
			}
			if (err == 1) {
				System.out.println("error");
			} else if (q.size() == 0) {
				System.out.println("[]");
			} else {
				int temp = q.size()-1;
				if (rdd == 0) {
					for (int j=0; j<temp; j++){
						sb.append(q.poll()).append(",");
					}
					sb.append(q.poll());
					sb.append("]");
				} else {
					for (int j=0; j<temp; j++){
						sb.append(q.pollLast()).append(",");
					}
					sb.append(q.pollLast());
					sb.append("]");
				}
				System.out.println(sb);
			}
		}
	}
}