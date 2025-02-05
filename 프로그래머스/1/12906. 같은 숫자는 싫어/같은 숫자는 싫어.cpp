#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    int cur = -1;
    for (const auto& x : arr) {
        if (cur != x) {
            cur = x;
            answer.push_back(x);
        }
    }

    return answer;
}