import java.io.*;
import java.util.*;

class Solution {
	
    public static void main(String [] args) throws Exception{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	StringBuilder sb = new StringBuilder();
    	int T = Integer.parseInt(br.readLine());
    	for (int tc = 1; tc<T+1; tc++) {
    		sb.append("#" + tc + " ");
    		int ans = 0;
    		st = new StringTokenizer(br.readLine());
    		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
    		HashMap<String, Integer> arr = new HashMap<>();
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<n; i++) {
				arr.put(st.nextToken(), 1);
    		}
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<m; i++) {
				String tem = st.nextToken();
				if (arr.containsKey(tem)) arr.put(tem,arr.get(tem)+1);
    		}
			Iterator arrIt = arr.keySet().iterator();
			while (arrIt.hasNext()) {
				if (arr.get(arrIt.next().toString()) == 2) ans++;
			}
			sb.append(ans + "\n");
    	}
    	System.out.println(sb);
    }
   
    
}