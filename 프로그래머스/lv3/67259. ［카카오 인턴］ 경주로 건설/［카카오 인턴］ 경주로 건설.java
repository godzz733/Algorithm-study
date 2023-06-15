import java.util.*;
class pos{
    int x,y,d;
    pos(int x, int y, int d){
        this.x = x;
        this.y = y;
        this.d = d;
    }
}
class Solution {
    static final int [] dx = {0,1,-1,0,0};
    static final int [] dy = {0,0,0,1,-1};
    static int [][] map;
    static int [][][] visited;
    static int n;
    public int solution(int[][] board) {
        n = board[0].length;
        map = new int[n][n];
        visited = new int[5][n][n];
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                map[i][j] = board[i][j];
                for (int k=0; k<5; k++){
                    visited[k][i][j] = 987654321;  
                }
            }
        }
        dfs();
        int answer = 987654321;
        for (int i=1; i<5; i++){
            answer = Math.min(answer, visited[i][n-1][n-1]);
        }
        return answer;
    }
    public static void dfs(){
        Deque<pos> q = new ArrayDeque<>();
        q.add(new pos(0,0,0));
        while (!q.isEmpty()){
            pos curr = q.poll();
            int x = curr.x, y = curr.y, d = curr.d;
            for (int i=1; i<5; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= n || map[nx][ny] == 1) continue;
                if (d == 0){
                    visited[i][nx][ny] = 100;
                    q.add(new pos(nx,ny,i));
                } else {
                    if (d != i){
                        if (visited[i][nx][ny] >= visited[d][x][y] + 600){
                            visited[i][nx][ny] = visited[d][x][y] + 600;
                            q.add(new pos(nx,ny,i));
                        }
                    } else {
                        if (visited[i][nx][ny] >= visited[d][x][y] + 100){
                            visited[i][nx][ny] = visited[d][x][y] + 100;
                            q.add(new pos(nx,ny,i));
                        }
                    }
                }
            }
        }
    }
}