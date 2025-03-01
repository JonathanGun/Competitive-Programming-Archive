#include <bits/stdc++.h>
using namespace std;

int main() {
    string s; cin >> s;
    int mx = 1;
    int cur = 1;
    char last = 'a';
    for(char c: s) {
        if (c != last) {
            cur = 1;
        } else {
            cur++;
            mx = max(mx, cur);
        }
        last = c;
    }
    cout << mx << endl;
}