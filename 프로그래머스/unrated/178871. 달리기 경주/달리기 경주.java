import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};
        Map<String,Integer> map = new HashMap();
        for (int i=0; i<players.length; i++){
            map.put(players[i],i);
        }
        for (int i=0; i<callings.length; i++){
            String tem = players[map.get(callings[i]) - 1];
            int idx = map.get(callings[i]);
            players[idx-1] = callings[i];
            players[idx] = tem;
            map.put(callings[i],idx-1);
            map.put(tem,idx);
        }
        return players;
    }
}