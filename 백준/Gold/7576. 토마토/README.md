# [Gold V] 토마토 - 7576 
## bfs
### 기본 구상

- 먼저 토마토는 내 상하좌우를 익게 하므로 바로 옆을 검사하는 bfs라고 판단
- 근데 하루가 지나면 기존에 있던 모든 토마토의 상하좌우가 익는다 → 그럼 횟수를 어떻게 할 것인가
- while문을 두개 써서 기존의 토마토 모두를 bfs를 돌리고 다 하면 + 1하는 방식으로 생각
- 그래서 한번 실행으로 익은 토마토를 바로 큐에 넣는게 아닌 리스트에 집어 넣어 다음 날에 다시 큐에 집어넣는 형식으로 짯음
- 마지막 반복문에서는 토마토가 다 익는게 불가능 한지를 판단
- 마지막 결과에서 cnt-1을 한 이유는 토마토가 다 익은 뒤 한번 더 연산을 하기 때문에 그걸 빼준거임
[문제 링크](https://www.acmicpc.net/problem/7576) 

### 성능 요약

메모리: 191036 KB, 시간: 440 ms

### 분류

너비 우선 탐색(bfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. </p>

<p style="text-align: center;"><img alt="" src="" style="width: 215px; height: 194px;"></p>

<p>창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.</p>

<p>토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.</p>

### 입력 

 <p>첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.</p>

<p>토마토가 하나 이상 있는 경우만 입력으로 주어진다.</p>

### 출력 

 <p>여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.</p>

