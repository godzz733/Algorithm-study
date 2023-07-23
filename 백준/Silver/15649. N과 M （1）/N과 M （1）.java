import java.io.*;
import java.util.*;
class Main{
    static int [] visited;
    static int n,m;
    static StringBuilder sb = new StringBuilder();
    static int [] tem,ans;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        tem = new int[m];
        visited = new int[n+1];
        back(0);
        System.out.println(sb);
    }
    static void back(int cnt){
        if (cnt == m){
            for (int i=0; i<m; i++){
                sb.append(tem[i] + " ");
            }
            sb.append('\n');
            return;
        }
        for (int i=1; i<=n; i++){
            if (visited[i] == 0){
                tem[cnt] = i;
                visited[i] = 1;
                back(cnt+1);
                visited[i] = 0;
            }
        }
    }
}