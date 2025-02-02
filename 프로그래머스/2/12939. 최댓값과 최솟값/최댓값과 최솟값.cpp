#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<int> arr;
    stringstream ss(s);
    string token;
    
    while (ss >> token){
        int num = stoi(token);
        arr.push_back(num);
    }
    
    int mx = *max_element(arr.begin(), arr.end());
    int mn = *min_element(arr.begin(), arr.end());
    
    return to_string(mn) + " " + to_string(mx);
}