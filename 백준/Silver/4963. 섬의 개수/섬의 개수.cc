#include<iostream>
#include<algorithm>
#include <deque>
#include <cstring>
using namespace std;

int n, m;
int arr[50][50];
deque<pair<int, int>> q;
int visited[50][50];
int dx[8] = { -1,-1,-1,0,1,1,1,0 }, dy[8] = { -1,0,1,1,1,0,-1,-1 };

void bfs(int x,int y) {
	visited[x][y] = 1;
	q.push_back(make_pair(x, y));
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop_front();
		for (int i = 0; i < 8; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m || visited[nx][ny] || !arr[nx][ny]) continue;
			visited[nx][ny] = 1;
			q.push_back(make_pair(nx, ny));
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	while (1) {
		int ans = 0;
		cin >> m >> n;
		if (!n && !m) return 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> arr[i][j];
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[i][j] && !visited[i][j]) {
					bfs(i, j);
					ans++;
				}
			}
		}
		cout << ans << '\n';
		memset(visited, 0, sizeof(visited));
	}
}