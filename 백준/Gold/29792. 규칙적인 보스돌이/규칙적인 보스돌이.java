import java.io.*;
import java.util.*;

class Pos{
	Long time,money;
	Pos(Long x,Long y){
		this.time = x;
		this.money = y;
	}
}
class Main {
	static StringBuilder sb = new StringBuilder();
	static int n,m,k;
	static Long tem;
	static ArrayList<Pos> arr;
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		arr = new ArrayList();
		int ans = 0;
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());	
		k = Integer.parseInt(st.nextToken());
		Long [] chr = new Long[n];
		for (int i=0; i<n; i++) {
			tem = Long.parseLong(br.readLine());
			chr[i] = tem;
		}
		for (int i=0; i<k; i++) {
			st = new StringTokenizer(br.readLine());
			Long a = Long.parseLong(st.nextToken());
			Long b = Long.parseLong(st.nextToken());
			arr.add(new Pos(a,b));
		}
		Arrays.sort(chr, Collections.reverseOrder());
		for (int i=0; i<m; i++) {
			tem = 0L;
			for (int j=0; j<(1<<k); j++) {
				Long money = 0L;
				Long temp = 0L;
				for (int q=0; q<k; q++) {
					if ((j & (1<<q)) != 0) {
						temp += (arr.get(q).time/chr[i])*chr[i] + (arr.get(q).time%chr[i] == 0 ? 0 : chr[i]);
						money += arr.get(q).money;
					}
				}
				if (temp <= chr[i] * 60 * 15) tem = Math.max(tem, money);
			}
			ans += tem;
		}
		System.out.println(ans);
			
	}
	
}