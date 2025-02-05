#include <vector>
#include <set>
#include <iostream>
using namespace std;

int solution(vector<int> nums)
{
    set<int> s(nums.begin(), nums.end());
    int x = nums.size() / 2;
    int k = s.size();
    
    if (x < k) {
        return x;
    } else {
        return k;
    }
    
}