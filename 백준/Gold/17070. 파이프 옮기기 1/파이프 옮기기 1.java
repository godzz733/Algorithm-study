import java.io.*;
import java.util.*;

class Pos{
    int x,y,pre;
    Pos(int x, int y, int pre){
        this.x = x;
        this.y = y;
        this.pre = pre;
    }
}
public class Main {
    static int n;
    static int [][] arr;
    static int[] dx = {0,1,1};
    static int[] dy = {1,1,0};
    static int ans = 0;
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        arr = new int [n][n];
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<n; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        pipe();
        System.out.println(ans);
    }
    
    static void pipe(){
        Deque<Pos> q = new ArrayDeque();
        q.push(new Pos(0,1,0));
        while (!q.isEmpty()){
            Pos curr = q.poll();
            int x = curr.x;
            int y = curr.y;
            int pre = curr.pre;
            for (int i=0; i<3; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || nx >= n || ny<0 || ny>=n || arr[nx][ny] == 1) continue;
                if (pre == 0){
                    if (i == 2) continue;
                } else if (pre == 2){
                    if (i == 0) continue;
                } 
                if (i == 1){
                    if (arr[nx-1][ny] == 1 || arr[nx][ny-1] == 1) continue;
                }
                if (nx == n-1 && ny == n-1) ans++;
                else q.push(new Pos(nx,ny,i));
            }
        }
    }
}