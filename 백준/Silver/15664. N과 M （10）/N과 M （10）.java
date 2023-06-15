import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main{
	
	static int n,m;
	static int[] arr;
	static int[] lst;
	static Set<String> visited;
	static boolean[] duplicate;
	static StringBuilder sb = new StringBuilder();
	static String result;
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		arr = new int[m];
		lst = new int[n];
		duplicate = new boolean[n];
		visited = new HashSet<String>();
		for (int i=0; i<n; i++) {
			lst[i] = sc.nextInt();
		}
		sc.close();
		Arrays.sort(lst);
		backtracking(0, 0);
		System.out.println(sb);
	}
	static void backtracking(int k, int depth) {
		if (depth==m) {
			result = "";
			for (int val:arr) {
				result += val + " ";
			}
			result += '\n';
			if (!visited.contains(result)) {
				sb.append(result);
				visited.add(result);
			}
			return;
		}
		for (int i=k; i<n; i++) {
			if (!duplicate[i]) {
				duplicate[i] = true;
				arr[depth] = lst[i];
				backtracking(i, depth+1);
				duplicate[i] = false;
			}
		}
	}
}
