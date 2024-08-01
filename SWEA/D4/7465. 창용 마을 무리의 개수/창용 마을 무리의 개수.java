
import java.util.*;
import java.io.*;

class Solution
{
    static ArrayList<ArrayList<Integer>> arr;
    static int [] lst;
    public static void main(String args[]) throws Exception
    {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for(int test_case = 1; test_case <= T; test_case++)
        {
            int ans = 0;
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            arr = new ArrayList<>();
            lst = new int[n+1];
            for (int i =0; i<=n; i++) arr.add(new ArrayList<>());
            for (int i=0; i<m; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                arr.get(a).add(b);
                arr.get(b).add(a);
            }
            for (int i=1; i<=n; i++) {
                if (lst[i] == 0) {
                    ans++;
                    solve(i);
                }
            }
            System.out.println("#"+test_case+" "+ans);
        }
    }

    static void solve(int x){
        for (int t: arr.get(x)) {
            if (lst[t] == 0) {
                lst[t] = 1;
                solve(t);
            }
        }
    }
}
