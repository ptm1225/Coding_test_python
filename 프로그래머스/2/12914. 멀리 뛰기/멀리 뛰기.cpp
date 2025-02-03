#include <string>
#include <vector>

using namespace std;

long long solution(int n) {
    vector<int> arr(n, 0);
    arr[0] = 1;
    arr[1] = 2;
    for (int i = 2; i < n; i++) {
        arr[i] = (arr[i-2] + arr[i-1]) % 1234567;
    }
    return arr[n-1];
}