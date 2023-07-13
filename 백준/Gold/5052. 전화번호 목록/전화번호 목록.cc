#include <iostream>
#include <vector>
using namespace std;
char tem[10000][11];

struct Trie
{
	bool finish;
	Trie* Node[10];

	Trie()
	{
		finish = false;
		for (int i = 0; i < 10; i++) {
			Node[i] = NULL;
		}
	}

	~Trie() {
		for (int i = 0; i < 26; i++) {
			if (Node[i]) {
				delete Node[i];
			}
		}
	}

	void insert(const char* key) {
		if (*key == '\0') {
			finish = true;
			return;
		}
		else {
			int curr = *key - '0';
			if (Node[curr] == NULL) {
				Node[curr] = new Trie();
			}
			Node[curr]->insert(key + 1);
		}
	}
	bool find(const char* key) {
		if (*key == '\0') {
			return false;
		}
		if (finish == true) {
			return true;
		}
		int curr = *key - '0';
		if (Node[curr] == NULL) return false;
		return Node[curr] -> find(key + 1);
	}
};
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n,t;
	cin >> n;
	for (int j = 0; j < n; j++) {
		cin >> t;
		Trie* trie = new Trie();
		string ans = "YES";
		for (int i = 0; i < t; i++) {
			cin >> tem[i];
			trie->insert(tem[i]);
		}
		int i;
		for (i = 0; i < t; i++) {
			if (trie->find(tem[i])) {
				cout << "NO" << "\n";
				break;
			}
		}
		if (i == t) {
			cout << "YES" << "\n";
		}
		
	}
	
	return 0;
	
}