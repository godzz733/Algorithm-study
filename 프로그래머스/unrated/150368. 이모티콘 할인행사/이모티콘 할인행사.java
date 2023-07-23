import java.util.*;
class Solution {
    static int ans_user = 0;
    static int ans_sum = 0;
    static int n,m;
    static int [][] arr;
    public int[] solution(int[][] users, int[] emoticons) {
        n = users.length;
        arr = new int[n][3];
        for (int i=0; i<n; i++){
            arr[i][0] = users[i][0];
            arr[i][1] = users[i][1];
        }
        back(0,emoticons);
        int [] answer = {ans_user,ans_sum};
        return answer;
    }
    static void back(int cnt, int[] emoticons){
        if (cnt == emoticons.length){
            int [] tem = plus();
            if (tem[0]>ans_user){
                ans_user = tem[0];
                ans_sum = tem[1];
            } else if (tem[0] == ans_user && tem[1]>ans_sum){
                ans_sum = tem[1];
            }
            return;
        }
        for (int i=1; i<=4; i++){
            int tem = emoticons[cnt] * (100-10*i)/100;
            for (int j=0; j<n; j++){
                if (10 * i >= arr[j][0]){
                    arr[j][2] += tem;
                }
            }
            back(cnt+1,emoticons);
            for (int j=0; j<n; j++){
                if (10 * i >= arr[j][0]){
                    arr[j][2] -= tem;
                }
            }
        }
    }
    static int[] plus(){
        int [] tem = new int[2];
        for (int i=0; i<n; i++){
            if (arr[i][2] >= arr[i][1]){
                tem[0]++;
            } else {
                tem[1] += arr[i][2];
            }
        }
        return tem;
    }
}