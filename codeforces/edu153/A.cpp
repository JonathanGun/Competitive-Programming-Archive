#include <bits/stdc++.h>
using namespace std;

string solve() {
    string s; cin >> s;
    if (s.length() == 1) return "";
    if (s == "()") return "";

}

int main() {
    int t; cin >> t;
    while(t--) {
        string ans = solve();
        if (ans.empty()) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
            cout << ans << endl;
        }
    }
}
