import java.io.*;
import java.util.*;

class pos{
	int x,y;
	pos(int x, int y){
		this.x = x;
		this.y = y;
	}
}
public class Main{
	static int n, m;
	static int [][] arr;
	static ArrayList<pos> chiken, house;
	static ArrayList<ArrayList<pos>> all;
	
	public static void main(String [] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken()); 
		m = Integer.parseInt(st.nextToken());
		int result = Integer.MAX_VALUE;
		arr = new int [n][n];
		chiken = new ArrayList<>();
		house = new ArrayList<>();
		all = new ArrayList<>();
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] == 1) {
					house.add(new pos(i,j));
				} else if (arr[i][j] == 2) {
					chiken.add(new pos(i,j));
				}
			}
		}
		for (int i=0 ; i<(1<<chiken.size()); i++) {
			ArrayList<pos> tem = new ArrayList<>();
			for (int j=0; j<chiken.size(); j++) {
				if ((i & 1<<j) != 0) {
					tem.add(chiken.get(j));
					if (tem.size()==m) {
						break;
					}
				}
			}
			all.add(tem);
		}
		for (int i=0; i<all.size(); i++) {
			ArrayList<pos> temp = all.get(i);
			int cnt = 0;
			for (int j=0; j<house.size(); j++) {
				int cnt1 = 10000;
				for (int k=0; k<temp.size(); k++) {
					cnt1 = Math.min(cnt1, Math.abs(house.get(j).x-temp.get(k).x)+ Math.abs(house.get(j).y-temp.get(k).y));
				}
				cnt += cnt1;
			}
			result = Math.min(result, cnt);
		}
		bw.write(result + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
}