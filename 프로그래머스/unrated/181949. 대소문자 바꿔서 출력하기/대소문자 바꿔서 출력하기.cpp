#include<iostream>
#include<string>

using namespace std;
string tem;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> tem;
	for (int i = 0; i < tem.size(); i++) {
		if (tem[i] >= 'A' && tem[i] <= 'Z') {
			tem[i] += 32;
		}
		else {
			tem[i] -= 32;
		}
	}
	cout << tem << '\n';
	
}