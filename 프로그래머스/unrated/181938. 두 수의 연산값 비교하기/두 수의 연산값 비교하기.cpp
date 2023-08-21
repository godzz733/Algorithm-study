#include <string>
#include <vector>
#include <cmath>
using namespace std;

int solution(int a, int b) {
    int answer = 0;
    
    string astr = to_string(a);
    string bstr = to_string(b);
    answer = max(a * pow(10, bstr.size()) + b, double(2 * a * b));

    return answer;
}